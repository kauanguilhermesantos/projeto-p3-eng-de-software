from abc import ABC, abstractmethod; 

class InterfaceSearchStrategy(ABC):
    @abstractmethod
    def search(self, cursor, query):
        pass

# class SearchStrategy:
#     def search(self, cursor, query):
#         raise NotImplementedError("Subclasses devem implementar o método search")

class SearchByTitle(InterfaceSearchStrategy):
    def search(self, cursor, title):
        cursor.execute("SELECT * FROM books WHERE name = %s", (title,))
        return cursor.fetchall()

class SearchByAuthor(InterfaceSearchStrategy):
    def search(self, cursor, author):
        cursor.execute("SELECT * FROM books WHERE author = %s", (author,))
        return cursor.fetchall()

class SearchByCategory(InterfaceSearchStrategy):
    def search(self, cursor, category):
        cursor.execute("SELECT * FROM books WHERE category = %s", (category,))
        return cursor.fetchall()
