from repositories.RegisterBook import RegisterBook
from repositories.BookSearchStrategy import *

from repositories.SearchBook import SearchBook

# db = Connection()
# cursor = db.get_cursor()

class Book:
    def __init__(self, connection):
        self.connection = connection
        self.register = RegisterBook()
        self.search = SearchBook()
    
    #função para registrar um livro
    def register_book(self):
        self.register.register_book(self.connection)
    
    #função para buscar um livro
    def search_book(self):
        self.search.search_book(self.connection)


