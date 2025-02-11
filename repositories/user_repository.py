from database.connection import connection, cursor

def register_user():
    user_name = input("Digite seu nome: ")
    user_email = input("Digite seu email: ")
    user_phone = input("Digite o número do seu telefone: ")
    try:
        cursor.execute('INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)', (user_name, user_email, user_phone))
        connection.commit()
        print('Parabéns, usuário cadastrado com sucesso!')
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)