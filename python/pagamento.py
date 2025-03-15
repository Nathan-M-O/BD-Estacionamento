from conexao import BancoDeDados

class Pagamento:
    def cadastrar(self, dados):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            agendamento = int(dados[0]) if dados[0] else None
            valor = float(dados[1].replace(',', '.'))
            forma = dados[2]
            
            cursor.execute(
                """INSERT INTO pagamentos 
                (cod_agendamento, valor_pag, forma_pag, data_pag)
                VALUES (%s, %s, %s, NOW())""",
                (agendamento, valor, forma)
            )
            conexao.commit()
            return True
        except ValueError as e:
            print(f"Valor inválido: {e}")
            return False
        except Exception as e:
            print(f"Erro ao registrar pagamento: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def listar(self):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM pagamentos")
            return cursor.fetchall()
        finally:
            cursor.close()
            conexao.close()
    
    def obter_por_cod(self, codigo):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM pagamentos WHERE cod_pagamento = %s", (codigo,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conexao.close()

    def atualizar(self, codigo, novos_dados):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            novos_dados = (
                int(novos_dados[0]) if novos_dados[0] else None,  # cod_agendamento
                float(novos_dados[1].replace(',', '.')) if novos_dados[1] else 0.0,  # valor
                novos_dados[2],
            )
            
            cursor.execute(
                """UPDATE pagamentos SET
                cod_agendamento = %s,
                valor_pag = %s,
                forma_pag = %s
                WHERE cod_pagamento = %s""",
                (*novos_dados, codigo)
            )
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar pagamento: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()


    def deletar(self, codigo):
        conexao = BancoDeDados.obter_conexao()
        cursor = conexao.cursor()
        try:
            cursor.execute("DELETE FROM pagamentos WHERE cod_pagamento = %s", (codigo,))
            conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao excluir pagamento: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()