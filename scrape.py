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
    d = pd.DataFrame(
        columns=['Sl_no', 'spider_id', 'industry', 'role', 'work_type', 'location', 'job_level',
                 'expected_wage', 'will_travel', 'will_relocate', 'objective', 'highest_degree',
                 'objective', 'experience', 'education', 'skills'])

    for i in page_data.find_all_next('a'):
        uri = i['href']
        if re.search(r'^/job/view-resume+html'):
            resume = up.urljoin('https://www.jobspider.com', uri)

        elif re.search(r'/page_[0-9]+', uri):
            page = up.urljoin('https://www.jobspider.com', uri)
            soup = BeautifulSoup(requests.get(page).content, 'lxml')
            links = soup.find_all('font')[13]


def get_resume():
    return

string = '/job/resume-search-results.asp/words_engineer/searchtype_1/page_4'
s = '/job/resume-search-results.asp/words_engineer/searchtype_1/sort_5'
# print(find_pattern(string))
def main ():
    url = 'https://www.jobspider.com/job/resume-search-results.asp/words_engineer/searchtype_1/page_3'
    site = requests.get(url)

    resume_doc = up.urljoin('https://www.jobspider.com', '/job/view-resume-78327.html')
    soup = BeautifulSoup(site.text, "lxml")
    links = soup.find_all('font')[13]
    # fetch_pages(links)
    soup_plus = BeautifulSoup(requests.get(resume_doc).text, 'lxml')
    # print(soup_plus.find('h1'))
    content = soup_plus.find(id='Table3').parent
    print(content.find_all('font').__len__())
    for i in soup_plus.find_all('font',attrs={'color': ['#000000', '#000f99']}):
        if re.search(r'Candidate|JobSpider', i.text) or not i.text:
            continue
        field = re.search(r'[a-zA-Z]+:', i.text)
        if field and not field.group()[0].islower():
            print(field.group()[:-1])
            print('PASSED:', i.text, end='\n----------\n')



if __name__ == "__main__":
    main()
