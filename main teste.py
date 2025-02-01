import mysql.connector
import questionary
from ClasseLivro import Livro
from Usuario import Usuario
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root123"
MYSQL_DB = "libra_tech"
MYSQL_PORT = 3307

connection = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB,
    port=MYSQL_PORT
)
# FAZER 3 classes: Livro, usuário, reserva

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

    cursor = connection.cursor()

    match(action):
        case 'Cadastrar livro':
            l = Livro()
            l.Cadastrar()
        case 'Cadastrar usuario':
            user = Usuario()
            user.CadastrarUsuario()
        case 'Fazer uma reserva':
            reserva = Usuario()
            reserva.FazerReserva()
        case 'Buscar um livro':
            busca = Livro()
            busca.BuscarLivro()
        case 'Sair':
            print("Saindo...")
            cursor.close()
            connection.close()
            break