class ReserveBook:
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