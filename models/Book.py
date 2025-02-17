from repositories.Interfaces import IRegisterBook, ISearchBook
from repositories.BookSearchStrategy import *


class Book:
    def __init__(self, connection, register: IRegisterBook, search: ISearchBook):
        self.connection = connection
        self.register = register  
        self.search = search  
    
    def register_book(self):
        self.register.register_book(self.connection)
    
    def search_book(self):
        self.search.search_book(self.connection)


