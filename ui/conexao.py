import mysql.connector

class BancoDeDados:
    @staticmethod
    def obter_conexao():
        try:
            return mysql.connector.connect(
                host='localhost',
                user='root',
                password='sua_senha',
                database='estaciona_facil'
            )
        except mysql.connector.Error as erro:
            print(f"Erro ao conectar ao banco de dados: {erro}")
            return None
