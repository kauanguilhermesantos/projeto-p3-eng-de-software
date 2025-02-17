import questionary

class RegisterBook:
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
                