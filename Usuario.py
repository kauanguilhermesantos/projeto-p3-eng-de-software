import questionary
import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root123"
MYSQL_DB = "libra_tech"
MYSQL_PORT = 3307

class Usuario:
    def __init__(self):
        self.connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        port=MYSQL_PORT
        )
        self.cursor = self.connection.cursor()

    def CadastrarUsuario(self):
        user_name = input("Digite seu nome: ")
        user_email = input("Digite seu email: ")
        user_phone = input("Digite o número do seu telefone: ")

        try:
            self.cursor.execute('INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)', (user_name, user_email, user_phone))
            self.connection.commit()
            print('Parabéns, usuário cadastrado com sucesso!')
        except Exception as e:
            print("Erro ao cadastrar usuário:", e)

    def FazerReserva(self):
        user_name = input("Digite o nome do usuário: ")
        self.cursor.execute('SELECT * FROM users WHERE name = %s', (user_name,))
        user_results = self.cursor.fetchall()

        if len(user_results) == 0:
            print('Erro: Usuário não encontrado.')
            return

        book_title = input("Digite o título do livro: ")
        self.cursor.execute('SELECT * FROM books WHERE name = %s', (book_title,))
        book_results = self.cursor.fetchall()

        if len(book_results) == 0:
            print('Erro: Livro não encontrado.')
            return

        book_id = book_results[0][0]  
        user_id = user_results[0][0]  

        try:
            self.cursor.execute('INSERT INTO reservations (bookId, userId) VALUES (%s, %s)', (book_id, user_id))
            self.connection.commit()
            print('Reserva feita com sucesso!')
        except Exception as e:
            print("Erro ao realizar reserva:", e)