import questionary
import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root123"
MYSQL_DB = "libra_tech"
MYSQL_PORT = 3307

class Livro:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=MYSQL_PORT
        )
        self.cursor = self.connection.cursor()
    
    def Cadastrar(self):
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
            self.cursor.execute('INSERT INTO books (name, category, author) VALUES (%s, %s, %s)', (book_name, category, author))
            self.connection.commit()
            print('Parabéns, livro cadastrado com sucesso!')
        except Exception as e:
            print("Erro ao cadastrar livro:", e)

    def BuscarLivro(self):
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
            self.cursor.execute('SELECT * FROM books WHERE name = %s', (book_title,))
            books = self.cursor.fetchall()

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)

        elif search_type == 'Buscar por Autor':
            author_name = input("Digite o nome do autor: ")
            self.cursor.execute('SELECT * FROM books WHERE author = %s', (author_name,))
            books = self.cursor.fetchall()

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
            self.cursor.execute('SELECT * FROM books WHERE category = %s', (category_name,))
            books = self.cursor.fetchall()

            if len(books) == 0:
                print("Livro não encontrado.")
            else:
                for book in books:
                    print(book)
