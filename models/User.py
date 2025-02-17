from repositories.Interfaces import IRegisterUser

class User:
    def __init__(self, connection, register: IRegisterUser):
        self.connection = connection
        self.register = register

    def register_user(self):
        self.register.register_user(self.connection)
