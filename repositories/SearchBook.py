import questionary
from database.Connection import Connection
from repositories.BookSearchStrategy import *

db = Connection()
cursor = db.get_cursor()

class SearchBook:
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
            books = strategy.search(cursor, book_title)

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)

        elif search_type == 'Buscar por Autor':
            author_name = input("Digite o nome do autor: ")
            strategy = SearchByAuthor()
            books = strategy.search(cursor, author_name)

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
            books = strategy.search(cursor, category_name)
            
            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)
