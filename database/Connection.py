import mysql.connector

class Connection:
    instance = None  # Armazena a única instância da classe
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Connection, cls).__new__(cls)
            cls.instance.connect()
        return cls.instance
    
    def connect(self):
        #Método privado para estabelecer a conexão com o banco de dados.
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="libra_tech",
            port=3307
        )
        self.cursor = self.connection.cursor()

    def get_connection(self):
        #Retorna a conexão ativa.
        return self.connection

    def get_cursor(self):
        #Retorna o cursor para executar consultas SQL.
        return self.cursor

    def close_connection(self):
        #Fecha a conexão com o banco de dados.
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            Connection.instance = None # Reseta a instância