import questionary

class Book:
    #função para registrar um livro
    def register_book(self, connect):
        book_name = input("Digite o nome do livro: ")
        category = questionary.select(
                "Qual a categoria do livro?",
                choices=[
                    'Esporte',
                    'Ficção',
                    'Educação',
                    'Fantasia',
                    'Diversa',
                ]
            ).ask()
        author = input("Qual o nome do autor do livro? ")
        try:
            connect.cursor.execute('INSERT INTO books (name, category, author) VALUES (%s, %s, %s)', (book_name, category, author))
            connect.connection.commit()
            print('Parabéns, livro cadastrado com sucesso!')
        except Exception as e:
            print("Erro ao cadastrar livro:", e)
    #função para reservar um livro
    def reserve_book(self, connect):
        user_name = input("Digite o nome do usuário: ")
        connect.cursor.execute('SELECT * FROM users WHERE name = %s', (user_name,))
        user_results = connect.cursor.fetchall()

        if len(user_results) == 0:
            print('Erro: Usuário não encontrado.')

        book_title = input("Digite o título do livro: ")
        connect.cursor.execute('SELECT * FROM books WHERE name = %s', (book_title,))
        book_results = connect.cursor.fetchall()

        if len(book_results) == 0:
            print('Erro: Livro não encontrado.')

        book_id = book_results[0][0]  
        user_id = user_results[0][0]  

        try:
            connect.cursor.execute('INSERT INTO reservations (bookId, userId) VALUES (%s, %s)', (book_id, user_id))
            connect.connection.commit()
            print('Reserva feita com sucesso!')
        except Exception as e:
            print("Erro ao realizar reserva:", e)
    #função para buscar um livro
    def search_book(self, connect):
        search_type = questionary.select(
                "Como você gostaria de buscar o livro?",
                choices=[
                    'Buscar por Título',
                    'Buscar por Autor',
                    'Buscar por Categoria'
                ]
            ).ask()

        if search_type == 'Buscar por Título':
            book_title = input("Digite o título do livro: ")
            connect.cursor.execute('SELECT * FROM books WHERE name = %s', (book_title,))
            books = connect.cursor.fetchall()

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)

        elif search_type == 'Buscar por Autor':
            author_name = input("Digite o nome do autor: ")
            connect.cursor.execute('SELECT * FROM books WHERE author = %s', (author_name,))
            books = connect.cursor.fetchall()

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
            connect.cursor.execute('SELECT * FROM books WHERE category = %s', (category_name,))
            books = connect.cursor.fetchall()

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)
