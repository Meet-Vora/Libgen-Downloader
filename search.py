from libgen_api import LibgenSearch
from bs4 import BeautifulSoup
import requests
libgen = LibgenSearch()


class SearchRequest():
    def __init__(self, is_fiction, author, title, year):
        self.base_fiction_url = 'https://libgen.is/fiction/'
        self.acceptable_extensions = ['epub']
        # self.language = 'English'

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
        results = []
        for format in self.acceptable_extensions:
            query = (self.author + ' ' + self.title).replace(' ', '+')
            url = self.base_fiction_url + '?q=' + query + '&format=' + format
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            if soup.body.p.string == 'No files were found.':
                return None
            # assuming that the content was found
            table_rows = soup.find('table', class_='catalog').tbody.find_all('tr')
            for row in table_rows:
                cols = row.find_all('td')
                title = cols[2].a.string
                extension = cols[4].string.split('/')[0].strip().lower()
                mirrors = [{'source': li.a['title'], 'url': li.a['href']} for li in cols[5].ul.find_all('li')]
                results.append({'title': title, 'extension': extension, 'mirrors': mirrors})
        return results

    def search(self):
        if self.is_fiction:
            return self._search_fictional()
        if not self.title:
            return self._search_author()
        return self._search_title()
