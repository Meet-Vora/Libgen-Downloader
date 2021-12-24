from libgen_api import LibgenSearch
from bs4 import BeautifulSoup
import requests
libgen = LibgenSearch()


class SearchRequest():
    def __init__(self, is_fiction, author, title, year):
        self.base_fiction_url = 'https://libgen.is/fiction/?q='
        self.is_fiction = is_fiction
        self.author = author
        self.title = title
        self.year = year
        
    def _search_title(self):
        """
        Search for nonfiction novel using the given title and filters.
        """
        return libgen.search_title(self.title)

    def _search_author(self):
        """
        Search for nonfiction novel using the given author and filters.
        """
        return libgen.search_author(self.author)

    def _search_fictional(self):
        """
        Search for fiction novel using the given author, title, and filters.
        """
        query = (self.author + ' ' + self.title).replace(' ', '+')
        url = self.base_fiction_url + query
        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # assuming that the content was found. Need to still check if the request found actual values
        table_rows = soup.find('table', class_='catalog').tbody.find_all('tr')
        print(len(table_rows))
    
    def search(self):
        if self.is_fiction:
            return self._search_fictional()
        if not self.title:
            return self._search_author()
        return self._search_title()
