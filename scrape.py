import requests
from bs4 import BeautifulSoup
import urllib.parse as up
import re


# table = soup.find_all('table')[4]
# print(table.find_all('table')[1])
# links = table.find_all('center')[1]
# for a in table.find_all('a'):
#     print(a['href'])


# print(page.prettify())
def fetch_pages(page_link):
    resume_doc = BeautifulSoup(requests.get(page_link).content, 'lxml')


def find_pattern(s:str):
    patt = re.search(r'/page_[0-9]+', s)
    try:
        return patt.string
    except AttributeError:
        return None

string = '/job/resume-search-results.asp/words_engineer/searchtype_1/page_4'
s = '/job/resume-search-results.asp/words_engineer/searchtype_1/sort_5'
# print(find_pattern(string))
def main ():
    url = 'https://www.jobspider.com/job/resume-search-results.asp/words_engineer/searchtype_1'
    site = requests.get(url)

    # resume_doc = up.urljoin('https://www.jobspider.com', '/job/view-resume-83943.html')
    soup = BeautifulSoup(site.text, "lxml")
    links = soup.find_all('font')[13]

if __name__ == "__main__":
    main()
