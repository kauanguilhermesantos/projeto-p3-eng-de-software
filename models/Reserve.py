from database.Connection import Connection
from repositories.ReserveBook import ReserveBook


# db = Connection()
# cursor = db.get_cursor()

class Reserve:
    def __init__(self, connection):
        self.connection = connection
        self.search = ReserveBook()
    #função para buscar um livro
    def reserve_book(self):
        self.reserve.reserve_book(self.connection)

