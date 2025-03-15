from conexao import BancoDeDados

class Vaga:
    def cadastrar(self, dados):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """INSERT INTO vagas 
                (numero_vaga, tipo_veiculo, disponivel)
                VALUES (%s, %s, %s)""",
                dados
            )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao cadastrar vaga: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def listar(self):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM vagas")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexao.close()

    def obter_por_cod(self, codigo):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM vagas WHERE cod_vaga = %s", (codigo,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, codigo, novo_numero, novo_tipo, novo_disponivel):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute(
                """UPDATE vagas SET 
                numero_vaga = %s, 
                tipo_veiculo = %s, 
                disponivel = %s 
                WHERE cod_vaga = %s""",
                (novo_numero, novo_tipo, novo_disponivel, codigo)
            )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar vaga: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def deletar(self, codigo):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM vagas WHERE cod_vaga = %s", (codigo,))
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar vaga: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()