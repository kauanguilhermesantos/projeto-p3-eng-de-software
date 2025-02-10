import mysql.connector

class Database:
    def __init__(self):
        self.MYSQL_HOST = "localhost"
        self.MYSQL_USER = "root"
        self.MYSQL_PASSWORD = "root123"
        self.MYSQL_DB = "libra_tech"
        self.MYSQL_PORT = 3307
        self.connection = None
        self.cursor = None

    def connect(self):
        """Estabelece a conexão com o banco de dados."""
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host=self.MYSQL_HOST,
                user=self.MYSQL_USER,
                password=self.MYSQL_PASSWORD,
                database=self.MYSQL_DB,
                port=self.MYSQL_PORT
            )
            self.cursor = self.connection.cursor()
        return self.cursor
    
    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.connection = None