
from repositories.RegisterUser import RegisterUser

class User:
    def __init__(self, connection):
        self.connection = connection
        self.register = RegisterUser()

    def register_user(self):
        self.register.register_user(self.connection)