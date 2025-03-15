from conexao import BancoDeDados

class Cliente:
    def cadastrar(self, dados):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)",
                dados
            )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def listar(self):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor(dictionary=True)  # ← Alteração aqui
        try:
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexao.close()

    def obter_por_cod(self, codigo):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM clientes WHERE cod_cliente = %s", (codigo,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, codigo, novos_dados):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """UPDATE clientes SET
                nome = %s, cpf = %s, telefone = %s, email = %s
                WHERE cod_cliente = %s""",
                (*novos_dados, codigo)
            )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar cliente: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def deletar(self, codigo):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM clientes WHERE cod_cliente = %s", (codigo,))
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir cliente: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()