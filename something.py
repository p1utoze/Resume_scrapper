from scrape import scrape
import argparse
import sys
parser = argparse.ArgumentParser(prog='scraper',
                                 description='A script to scrape Resumes of various domains'
                                             'listed in www.jobspider.com',
                                 allow_abbrev=True,)

# no_args_group = parser.add_mutually_exclusive_group(required=False)
# no_args_group.add_argument('-d', '--description', action='store_true', help='Print program description')

myargs_group = parser.add_mutually_exclusive_group(required=False)
myargs_group.add_argument('-n', '--domain', type=str, action='store')
myargs_group.add_argument('-c', '--category', action='store')
args = parser.parse_args()

if args.domain:
    print('hi')

else:
    print(parser.description)
    print('Running default search: engineer.....')
    d = scrape()
    exit()