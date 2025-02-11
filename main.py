import questionary
from database.Connection import Connection
from repositories.Book import Book
from repositories.User import User

book = Book()
user = User()
connect = Connection()

while True:
    action = questionary.select(
        "O que você deseja fazer?",
        choices=[
            'Cadastrar livro',
            'Cadastrar usuario',
            'Fazer uma reserva',
            'Buscar um livro',
            'Sair'
        ]
    ).ask()

    if action == "Cadastrar livro":
        book.register_book(connect)

    elif action == "Cadastrar usuario":
        user.register_user(connect)

    elif action == "Fazer uma reserva":
        book.reserve_book(connect)

    elif action == "Buscar um livro":
        book.search_book(connect)

    elif action == "Sair":
        print("Saindo...")
        connect.cursor.close()
        connect.connection.close()
        break
    else:
        print("Opção inválida. Tente novamente.")
