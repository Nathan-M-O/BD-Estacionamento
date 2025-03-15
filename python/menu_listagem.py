class MenuListagem:
    def __init__(self, cliente, vaga, pagamento):
        self.cliente = cliente
        self.vaga = vaga
        self.pagamento = pagamento

    def exibir(self):
        while True:
            print("\n=== LISTAR ===")
            print("1. Clientes")
            print("2. Vagas")
            print("3. Pagamentos")
            print("4. Voltar")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.listar_clientes()
                case '2': self.listar_vagas()
                case '3': self.listar_pagamentos()
                case '4': break
                case _: print("Opção inválida!")

    def listar_clientes(self):
        print("\n--- Clientes Cadastrados ---")
        clientes = self.cliente.listar()
        for cliente in clientes:
            print(f"""
            ID: {cliente['cod_cliente']}
            Nome: {cliente['nome']}
            CPF: {cliente['cpf']}
            Telefone: {cliente['telefone']}
            Email: {cliente['email']}
            ----------------------------""")

    def listar_vagas(self):
        print("\n--- Vagas Cadastradas ---")
        vagas = self.vaga.listar()
        for vaga in vagas:
            status = "Disponível" if vaga['disponivel'] else "Ocupada"
            print(f"""
            ID: {vaga['cod_vaga']}
            Número: {vaga['numero_vaga']}
            Tipo: {vaga['tipo_veiculo']}
            Status: {status}
            ----------------------------""")

    def listar_pagamentos(self):
        print("\n--- Pagamentos Registrados ---")
        pagamentos = self.pagamento.listar()
        for pgto in pagamentos:
            print(f"""
            ID: {pgto['cod_pagamento']}
            Agendamento: {pgto['cod_agendamento']}
            Valor: R$ {pgto['valor_pag']:.2f}
            Forma: {pgto['forma_pag']}
            Data: {pgto['data_pag']}
            ----------------------------""")