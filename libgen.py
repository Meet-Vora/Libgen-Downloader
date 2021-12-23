import pyinputplus as pyip
from search import SearchRequest
from pprint import pprint

def menu():
    is_fiction = True if pyip.inputMenu(prompt="\nWhat category does your text fall into?\n", choices=[
        "Fiction", "Non-fiction"], numbered=True) == 'Fiction' else False
    # if is_fiction:
    print('\n')

    while True:
        author = pyip.inputStr(prompt="Author: ", blank=True)
        title = pyip.inputStr(prompt="Title: ", blank=True)

        if not author and not title:
            print('\nYou cannot leave both author and title fields empty. Please enter in at least one')
            continue

        year = pyip.inputNum(prompt="Year: ", blank=True) # can parse the input for 0 <= year <= current year
        break

    return {'is_fiction': is_fiction, 'author': author, 'title': title, 'year': year}

    # extension = pyip.


if __name__ == "__main__":
    inputs = menu()
    searchrequest = SearchRequest(is_fiction=inputs['is_fiction'], title=inputs['title'], author=inputs['author'], year=inputs['year'])
    # pprint(search_title("the sword of kaigen"))