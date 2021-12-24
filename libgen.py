import pyinputplus as pyip
from argparse import ArgumentParser
from search import SearchRequest
from pprint import pprint

test_is_fiction = True
test_title = 'sword of kaigen'
test_author = 'wang'
test_year = None

def menu():
    is_fiction = True if pyip.inputMenu(prompt="\nWhat category does your text fall into?\n", choices=[
        "Fiction", "Non-fiction"], numbered=True) == 'Fiction' else False
    # if is_fiction:
    print('\n')

    while True:
        author = pyip.inputStr(prompt="Author: ", blank=True)
        title = pyip.inputStr(prompt="Title: ", blank=True)

        if author or title:
            year = pyip.inputNum(prompt="Year: ", blank=True) # can parse the input for 0 <= year <= current year
            break

        print('\nYou cannot leave both author and title fields empty. Please enter in at least one')

    return {'is_fiction': is_fiction, 'author': author.lower(), 'title': title.lower(), 'year': year}

    # extension = pyip.


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()

    if args.debug:
        searchrequest = SearchRequest(is_fiction=test_is_fiction, title=test_title, author=test_author, year=test_year)
    else:
        inputs = menu()
        searchrequest = SearchRequest(is_fiction=inputs['is_fiction'], title=inputs['title'], author=inputs['author'], year=inputs['year'])
    searchrequest.search()
    # pprint(search_title("the sword of kaigen"))