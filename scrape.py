import requests
from bs4 import BeautifulSoup
import urllib.parse as up
import pandas as pd
import re


# table = soup.find_all('table')[4]
# print(table.find_all('table')[1])
# links = table.find_all('center')[1]
# for a in table.find_all('a'):
#     print(a['href'])


# print(page.prettify())
def fetch_pages(page_data):
    d = {}

    for i in page_data.find_all_next('a'):
        uri = i['href']
        if re.search(r'^/job/view-resume+html', uri):
            resume = up.urljoin('https://www.jobspider.com', uri)
            for key, value in get_resume(resume):
                d[key] = d.get(key, value)

        elif re.search(r'/page_[0-9]+', uri):
            page = up.urljoin('https://www.jobspider.com', uri)
            soup = BeautifulSoup(requests.get(page).content, 'lxml')
            links = soup.find_all('font')[13]


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
# print(find_pattern(string))
def main ():
    url = 'https://www.jobspider.com/job/resume-search-results.asp/words_engineer/searchtype_1/page_3'
    site = requests.get(url)

    resume_doc = up.urljoin('https://www.jobspider.com', '/job/view-resume-78327.html')
    soup = BeautifulSoup(site.text, "lxml")
    links = soup.find_all('font')[13]
    fetch_pages(links)
    soup_plus = BeautifulSoup(requests.get(resume_doc).text, 'lxml')
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
