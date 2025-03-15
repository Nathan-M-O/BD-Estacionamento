from cliente import Cliente
from vaga import Vaga
from pagamento import Pagamento
from menu_cadastro import MenuCadastro
from menu_listagem import MenuListagem
from menu_gerenciamento import MenuGerenciamento

class SistemaEstacionamento:
    def __init__(self):
        self.cliente = Cliente()
        self.vaga = Vaga()
        self.pagamento = Pagamento()
        
        self.menu_cadastro = MenuCadastro(self.cliente, self.vaga, self.pagamento)
        self.menu_listagem = MenuListagem(self.cliente, self.vaga, self.pagamento)
        self.menu_gerenciamento = MenuGerenciamento(self.cliente, self.vaga, self.pagamento)

    def iniciar(self):
        while True:
            print("\n=== MENU PRINCIPAL ===")
            print("1. Cadastrar")
            print("2. Listar")
            print("3. Gerenciar")
            print("4. Sair")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.menu_cadastro.exibir()
                case '2': self.menu_listagem.exibir()
                case '3': self.menu_gerenciamento.exibir()
                case '4': break
                case _: print("Opção inválida!")