def return_books(books):
    if len(books) == 0:
        print("Livro não encontrado.")
    else:
        for book in books:
            print(book)

class SearchStrategy:
    def search(self, cursor, query):
        raise NotImplementedError("Subclasses devem implementar o método search")

class SearchByTitle(SearchStrategy):
    def search(self, cursor, title):
        cursor.execute("SELECT * FROM books WHERE name = %s", (title,))
        return cursor.fetchall()

class SearchByAuthor(SearchStrategy):
    def search(self, cursor, author):
        cursor.execute("SELECT * FROM books WHERE author = %s", (author,))
        return cursor.fetchall()

class SearchByCategory(SearchStrategy):
    def search(self, cursor, category):
        cursor.execute("SELECT * FROM books WHERE category = %s", (category,))
        return cursor.fetchall()
