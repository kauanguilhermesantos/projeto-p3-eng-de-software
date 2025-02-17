import questionary
from database.Connection import Connection
from models.Book import Book
from models.User import User

connect = Connection()
book = Book(connect)
user = User(connect)

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
        book.register_book()

    elif action == "Cadastrar usuario":
        user.register_user()

    elif action == "Fazer uma reserva":
        book.reserve_book()

    elif action == "Buscar um livro":
        book.search_book()

    elif action == "Sair":
        print("Saindo...")
        connect.cursor.close()
        connect.connection.close()
        break
    else:
        print("Opção inválida. Tente novamente.")
