from libgen_api import LibgenSearch
from bs4 import BeautifulSoup
import requests
libgen = LibgenSearch()

BASE_URL = 'libgen.is/fiction?q='

class SearchRequest():
    def __init__(self, is_fiction, author, title, year):
        self.is_fiction = is_fiction
        self.author = author
        self.title = title
        
    def search_title(title, filters):
        """
        Search for nonfiction novel using the given title and filters.
        """
        return libgen.search_title(title)

    def search_author(author, filters):
        """
        Search for nonfiction novel using the given author and filters.
        """
        return libgen.search_author(author)

    def search_query(author, title, filters):
        """
        Search for fiction novel using the given author, title, and filters.
        """
        query = author + title