import questionary
from repositories.BookSearchStrategy import *
from .Interfaces import ISearchBook

class SearchBook(ISearchBook):
    def search_book(self, connect):
        search_type = questionary.select(
                "Como você gostaria de buscar o livro?",
                choices=[
                    'Buscar por Título',
                    'Buscar por Autor',
                    'Buscar por Categoria'
                ]
            ).ask()
        
        strategy = None

        if search_type == 'Buscar por Título':
            book_title = input("Digite o título do livro: ")
            strategy = SearchByTitle()
            books = strategy.search(connect.cursor, book_title)

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)

        elif search_type == 'Buscar por Autor':
            author_name = input("Digite o nome do autor: ")
            strategy = SearchByAuthor()
            books = strategy.search(connect.cursor, author_name)

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)

        elif search_type == 'Buscar por Categoria':
            category_choices = [
                    'Esporte',
                    'Ficção',
                    'Educação',
                    'Fantasia',
                    'Diversa'
                ]
            category_name = questionary.select(
                    "Escolha a categoria do livro:",
                    choices=category_choices
                ).ask()
            strategy = SearchByCategory()
            books = strategy.search(connect.cursor, category_name)
            
            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)
