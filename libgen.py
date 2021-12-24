from libgen_api import LibgenSearch
import pyinputplus as pyip
import requests
import re
import os
from argparse import ArgumentParser
from search import SearchRequest
from pprint import pprint
libgen = LibgenSearch()

test_is_fiction = True
test_title = 'sword of kaigen'
test_author = 'wang'
test_year = None


def menu():
    is_fiction = True if pyip.inputMenu(prompt="\nWhat category does your text fall into?\n", choices=[
        "Fiction", "Non-fiction"], numbered=True) == 'Fiction' else False
    # if is_fiction:
    print('\n')

    # while True:
    title = pyip.inputStr(prompt="Title: ")
    author = pyip.inputStr(prompt="Author: ", blank=True)
    year = pyip.inputNum(prompt="Year: ", blank=True) # can parse the input for 0 <= year <= current year

        # print('\nYou cannot leave both author and title fields empty. Please enter in at least one')

    return {'is_fiction': is_fiction, 'author': author.lower(), 'title': title.lower(), 'year': year}


def write_file(download_links, path="/home/meetv/Documents/Books"):
    response = requests.get(download_links['GET'], allow_redirects=True)
    filename = getFilename_fromCd(response.headers.get('content-disposition')) 
    with open(os.path.join(path, filename), 'wb') as file:
        file.write(response.content)
        print('Wrote file!')


def getFilename_fromCd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-f', '--fast', action='store_true')
    args = parser.parse_args()

    if args.fast:
        searchrequest = SearchRequest(is_fiction=test_is_fiction, title=test_title, author=test_author, year=test_year)
    else:
        inputs = menu()
        searchrequest = SearchRequest(is_fiction=inputs['is_fiction'], title=inputs['title'], author=inputs['author'], year=inputs['year'])
    results = searchrequest.search()
    # resolving first result's first mirror link into a download link. Passed in hardcoded
    # dictionary by looking at LibgenAPI's source code: https://github.com/harrison-broadbent/libgen-api/blob/master/libgen_api/libgen_search.py#L33-L39
    download_links = libgen.resolve_download_links({'Mirror_1': results[0]['mirrors'][0]['url']})
    write_file(download_links)