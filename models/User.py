
from repositories.RegisterUser import RegisterUser

class User:
    def __init__(self, connection):
        self.connection = connection
        self.register = RegisterUser()

    def register_user(self):
        self.register.register_user(self.connection)

    # def register_user(self, connect):
    #     user_name = input("Digite seu nome: ")
    #     user_email = input("Digite seu email: ")
    #     user_phone = input("Digite o número do seu telefone: ")
    #     try:
    #         connect.cursor.execute('INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)', (user_name, user_email, user_phone))
    #         connect.connection.commit()
    #         print('Parabéns, usuário cadastrado com sucesso!')
    #     except Exception as e:
    #         print("Erro ao cadastrar usuário:", e)