class MenuCadastro:
    def __init__(self, cliente, vaga, pagamento):
        self.cliente = cliente
        self.vaga = vaga
        self.pagamento = pagamento

    def exibir(self):
        while True:
            print("\n=== CADASTRAR ===")
            print("1. Cliente")
            print("2. Vaga")
            print("3. Pagamento")
            print("4. Voltar")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.cadastrar_cliente()
                case '2': self.cadastrar_vaga()
                case '3': self.cadastrar_pagamento()
                case '4': break
                case _: print("Opção inválida!")

    def cadastrar_cliente(self):
        print("\n--- Novo Cliente ---")
        dados = (
            input("Nome: "),
            input("CPF: "),
            input("Telefone: "),
            input("Email: ")
        )
        if self.cliente.cadastrar(dados):
            print("Cliente cadastrado com sucesso!")

    def cadastrar_vaga(self):
        print("\n--- Nova Vaga ---")
        numero = input("Número: ")
        tipo = input("Tipo de veículo: ")
        disponivel = 1 if input("Disponível (S/N): ").upper() == 'S' else 0
        
        if self.vaga.cadastrar((numero, tipo, disponivel)):
            print("Vaga cadastrada com sucesso!")

    def cadastrar_pagamento(self):
        print("\n--- Novo Pagamento ---")
        agendamento = input("Código do agendamento (opcional): ").strip() or None
        valor = input("Valor: ")
        forma = input("Forma de pagamento: ")
        
        try:
            if self.pagamento.cadastrar((agendamento, valor, forma)):
                print("Pagamento registrado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")