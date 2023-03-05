import requests
from bs4 import BeautifulSoup
import urllib.parse as up
import pandas as pd
import re

# print(page.prettify())
def fetch_pages(page_data):
    for i in page_data.find_all_next('a'):
        uri = i['href']
        if re.search(r'/page_[0-9]+', uri):
            page = up.urljoin('https://www.jobspider.com', uri)
            # soup = BeautifulSoup(requests.get(page).content, 'lxml')
            yield page


def resume_links(page_data, d):
    # print(*[i['href']for i in page_data.find_all('a')], sep='\n')
    for i in page_data.find_all('a'):
        uri = i['href']
        if re.search(r'^/job/view-resume+', uri):
            resume = up.urljoin('https://www.jobspider.com', uri)
            print('Extracting page: ', resume, '\n......')
            for key, value in get_resume(resume):
                if not d.get(key, None):
                    d[key] = [value]
                else:
                    d[key].append(value)
    return d

def get_resume(doc):
    soup = BeautifulSoup(requests.get(doc).text, 'lxml')
    for i in soup.find_all('font', attrs={'color': ['#000000', '#000f99']}):
        if re.search(r'Candidate|JobSpider', i.text) or not i.text:
            continue
        field = re.search(r'[a-zA-Z]+:', i.text)
        if field and not field.group()[0].islower():
            yield field.group()[:-1], re.sub(r'[a-zA-Z]+:', '', i.text)

# string = '/job/resume-search-results.asp/words_engineer/searchtype_1/page_4'
# s = '/job/resume-search-results.asp/words_engineer/searchtype_1/sort_5'
# s = '/job/view-resume-83943.html'
# print(re.match(r'^/job/view-resume+', s).string)
def main ():
    url = 'https://www.jobspider.com/job/resume-search-results.asp/words_engineer/searchtype_1'
    site = requests.get(url)
    check_pages = {}
    resume_doc = up.urljoin('https://www.jobspider.com', '/job/view-resume-78327.html')
    soup = BeautifulSoup(site.text, "lxml")
    links = soup.find_all('font')[13]
    d = resume_links(links, {})
    print(d.keys())
    for page in fetch_pages(links):
        if not check_pages.get(page, None):
            check_pages[page] = 1
            # print('FETCHED: ', page)
    # soup_plus = BeautifulSoup(requests.get(resume_doc).text, 'lxml')
    # content = soup_plus.find(id='Table3').parent
    # for i in soup_plus.find_all('font', attrs={'color': ['#000000', '#000f99']}):
    #     if re.search(r'Candidate|JobSpider', i.text) or not i.text:
    #         continue
    #     field = re.search(r'[a-zA-Z]+:', i.text)
    #     if field and not field.group()[0].islower():
    #         print(field.group()[:-1])
    #         content = re.sub(r'[a-zA-Z]+:', '', i.text)
    #         print('CONTENT:', content, end='\n----------\n')


if __name__ == "__main__":
    main()
