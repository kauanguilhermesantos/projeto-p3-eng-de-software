from repositories.Interfaces import IReserveBook

class Reserve:
    def __init__(self, connection, reserve: IReserveBook):
        self.connection = connection
        self.reserve = reserve 

    def reserve_book(self):
        self.reserve.reserve_book(self.connection)

