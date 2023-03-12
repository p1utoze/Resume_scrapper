from scrape import scrape
import argparse
import sys
parser = argparse.ArgumentParser(
                                 description='A script to scrape Resumes of various domains'
                                             'listed in www.jobspider.com',
                                 allow_abbrev=True)

no_args_group = parser.add_mutually_exclusive_group(required=False)
no_args_group.add_argument('-d', '--description', action='store_true', help='Print program description')

# parser.add_argument('')
args = parser.parse_args()

if args.description:
    print('hi')
else:
    print(parser.description)
    exit()