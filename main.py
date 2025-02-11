import questionary
from database.connection import connection, cursor
from repositories.book_repository import register_book, reserve_book, search_book
from repositories.user_repository import register_user

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
        register_book()

    elif action == "Cadastrar usuario":
        register_user()

    elif action == "Fazer uma reserva":
        reserve_book()

    elif action == "Buscar um livro":
        search_book()
        
    elif action == "Sair":
        print("Saindo...")
        cursor.close()
        connection.close()
        break

    else:
        print("Opção inválida. Tente novamente.")
