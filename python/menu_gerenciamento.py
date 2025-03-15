class MenuGerenciamento:
    def __init__(self, cliente, vaga, pagamento):
        self.cliente = cliente
        self.vaga = vaga
        self.pagamento = pagamento

    def exibir(self):
        while True:
            print("\n=== GERENCIAR ===")
            print("1. Clientes")
            print("2. Vagas")
            print("3. Pagamentos")
            print("4. Voltar")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.gerenciar_clientes()
                case '2': self.gerenciar_vagas()
                case '3': self.gerenciar_pagamentos()
                case '4': break
                case _: print("Opção inválida!")

# ---------------------------------------- GERENCIAMENTO DE CLIENTES ----------------------------------------
    def gerenciar_clientes(self):
        while True:
            print("\n--- Gerenciar Clientes ---")
            print("1. Atualizar")
            print("2. Excluir")
            print("3. Voltar")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.atualizar_cliente()
                case '2': self.excluir_cliente()
                case '3': break
                case _: print("Opção inválida!")

    def atualizar_cliente(self):
        print("\n--- Atualizar Cliente ---")
        codigo = input("Código do cliente: ")
        cliente = self.cliente.obter_por_cod(codigo)
        
        if not cliente:
            print("Cliente não encontrado!")
            return
            
        novos_dados = (
            input(f"Nome atual ({cliente['nome']}): ") or cliente['nome'],
            input(f"CPF atual ({cliente['cpf']}): ") or cliente['cpf'],
            input(f"Telefone atual ({cliente['telefone']}): ") or cliente['telefone'],
            input(f"Email atual ({cliente['email']}): ") or cliente['email']
        )
        
        if self.cliente.atualizar(codigo, novos_dados):
            print("Cliente atualizado com sucesso!")

    def excluir_cliente(self):
        print("\n--- EXCLUIR CLIENTE ---")
        codigo = input("Código do cliente: ")
        confirmacao = input("Tem certeza? (s/n): ").lower()
        
        if confirmacao == 's':
            self.cliente.deletar(codigo)
            print("Cliente excluído com sucesso!")

# ---------------------------------------- GERENCIAMENTO DE VAGAS ---------------------------------------
    def gerenciar_vagas(self):
        while True:
            print("\n--- Gerenciar Vagas ---")
            print("1. Atualizar")
            print("2. Excluir")
            print("3. Voltar")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.atualizar_vaga()
                case '2': self.excluir_vaga()
                case '3': break
                case _: print("Opção inválida!")
    
    def atualizar_vaga(self):
        print("\n--- ATUALIZAR VAGA ---")
        codigo = input("Código da vaga: ")
        vaga = self.vaga.obter_por_cod(codigo)
        
        if not vaga:
            print("Vaga não encontrada!")
            return
        
        novo_numero = input(f"Número atual ({vaga['numero_vaga']}): ") or vaga['numero_vaga']
        novo_tipo = input(f"Tipo atual ({vaga['tipo_veiculo']}): ") or vaga['tipo_veiculo']
        
        disponivel_input = input(f"Disponível? (S/N) [Atual: {'S' if vaga['disponivel'] else 'N'}]): ").upper()
        novo_disponivel = 1 if disponivel_input == 'S' else 0 if disponivel_input == 'N' else vaga['disponivel']
        
        if self.vaga.atualizar(codigo, novo_numero, novo_tipo, novo_disponivel):
            print("Vaga atualizada com sucesso!")

    def excluir_vaga(self):
        print("\n--- EXCLUIR VAGA ---")
        codigo = input("Código da vaga: ")
        confirmacao = input("Tem certeza? (s/n): ").lower()
        
        if confirmacao == 's':
            self.vaga.deletar(codigo)
            print("Vaga excluída com sucesso!")

# ---------------------------------------- GERENCIAMENTO DE PAGAMENTOS ---------------------------------------
    def gerenciar_pagamentos(self):
        while True:
            print("\n--- Gerenciar Pagamentos ---")
            print("1. Atualizar")
            print("2. Excluir")
            print("3. Voltar")
            
            opcao = input("Escolha: ")
            
            match opcao:
                case '1': self.atualizar_pagamento()
                case '2': self.excluir_pagamento()
                case '3': break
                case _: print("Opção inválida!")
    
    def atualizar_pagamento(self):
        print("\n--- ATUALIZAR PAGAMENTO ---")
        codigo = input("Código do pagamento: ")
        pagamento = self.pagamento.obter_por_cod(codigo)
        
        if not pagamento:
            print("Pagamento não encontrado!")
            return
        
        novo_agendamento = input(f"Agendamento atual ({pagamento['cod_agendamento']}): ").strip() or pagamento['cod_agendamento']
        novo_valor = input(f"Valor atual ({pagamento['valor_pag']}): ") or pagamento['valor_pag']
        nova_forma = input(f"Forma atual ({pagamento['forma_pag']}): ") or pagamento['forma_pag']
        
        if self.pagamento.atualizar(codigo, (novo_agendamento, novo_valor, nova_forma)):
            print("Pagamento atualizado com sucesso!")

    def excluir_pagamento(self):
        print("\n--- EXCLUIR PAGAMENTO ---")
        codigo = input("Código do pagamento: ")
        confirmacao = input("Tem certeza? (s/n): ").lower()
        
        if confirmacao == 's':
            self.pagamento.deletar(codigo)
            print("Pagamento excluído com sucesso!")