import mysql.connector

class BancoDeDados:
    @staticmethod
    def obter_conexao():
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='Macaxeira132@',
            database='estaciona_facil'
        )