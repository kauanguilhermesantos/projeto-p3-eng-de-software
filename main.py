import questionary
from database.Connection import Connection
from models.Book import Book
from models.User import User
from models.Reserve import Reserve

from repositories.RegisterUser import RegisterUser
from repositories.RegisterBook import RegisterBook
from repositories.SearchBook import SearchBook
from repositories.ReserveBook import ReserveBook

connect = Connection()
register_user = RegisterUser()
register_book = RegisterBook()
search_book = SearchBook()
reserve_book = ReserveBook()

user = User(connect, register_user)
book = Book(connect, register_book, search_book)
reserve = Reserve(connect, reserve_book)

while True:
    action = questionary.select(
        "O que você deseja fazer?",
        choices=[
            'Cadastrar livro',
            'Cadastrar usuário',
            'Fazer uma reserva',
            'Buscar um livro',
            'Sair'
        ]
    ).ask()

    if action == "Cadastrar livro":
        book.register_book()

    elif action == "Cadastrar usuário":
        user.register_user()

    elif action == "Fazer uma reserva":
        reserve.reserve_book()

    elif action == "Buscar um livro":
        book.search_book()

    elif action == "Sair":
        print("Saindo...")
        connect.cursor.close()
        connect.connection.close()
        break
    else:
        print("Opção inválida. Tente novamente.")