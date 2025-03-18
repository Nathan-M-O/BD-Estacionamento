import tkinter as tk
from tkinter import messagebox
from datetime import datetime

clientes = []
pagamentos = []

vagas = {i: True for i in range(1, 33)}

# cores e fontes
cor_principal = "#2c3e50"
cor_secundaria = "#3498db"
cor_texto = "#333333"
cor_fundo = "white"
cor_botao = "#7f8c8d"
cor_botao_texto = "white"
fonte_titulo = ("Arial", 24, "bold")
fonte_subtitulo = ("Arial", 18)
fonte_texto = ("Arial", 12)

# função para cadastrar carro
def cadastrar_carro(cliente, valor_pagamento, vaga):
    carro_janela = tk.Toplevel(cadastro_janela)
    carro_janela.title("Dados do Carro")
    carro_janela.geometry("300x320")
    carro_janela.configure(bg=cor_fundo)

    modelo_label = tk.Label(carro_janela, text="Modelo:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    modelo_label.pack(pady=5)
    modelo_entry = tk.Entry(carro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    modelo_entry.pack(padx=20, pady=5, fill="x")

    placa_label = tk.Label(carro_janela, text="Placa:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    placa_label.pack(pady=5)
    placa_entry = tk.Entry(carro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    placa_entry.pack(padx=20, pady=5, fill="x")

    cor_label = tk.Label(carro_janela, text="Cor:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    cor_label.pack(pady=5)
    cor_entry = tk.Entry(carro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    cor_entry.pack(padx=20, pady=5, fill="x")

    def salvar_carro():
        cliente["Carro"] = {
            "Modelo": modelo_entry.get(),
            "Placa": placa_entry.get(),
            "Cor": cor_entry.get()
        }
        carro_janela.destroy()
        messagebox.showinfo("Cadastro", f"Cliente cadastrado com sucesso! Valor do pagamento: R$ {valor_pagamento},00, Vaga {vaga} ocupada.")
        cadastro_janela.destroy()

    salvar_btn = tk.Button(carro_janela, text="Salvar", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto, command=salvar_carro)
    salvar_btn.pack(pady=20, padx=20, fill="x")

def cadastrar_cliente():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    telefone = telefone_entry.get()
    vaga = vaga_entry.get()
    tempo = tempo_entry.get()
    forma_pagamento = pagamento_var.get()

    if not nome or not cpf or not email or not telefone or not vaga or not tempo or not forma_pagamento:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    try:
        vaga = int(vaga)
        tempo = int(tempo)
        if vaga < 1 or vaga > 32 or tempo <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido para a vaga ou o tempo.")
        return

    if not vagas[vaga]:
        messagebox.showerror("Erro", "Esta vaga já está ocupada.")
        return

    for cliente in clientes:
        if cliente["CPF"] == cpf:
            messagebox.showerror("Erro", "Já existe um cliente com este CPF.")
            return

    valor_pagamento = 50 * tempo
    data_pagamento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    cliente = {"Nome": nome, "CPF": cpf, "Email": email, "Telefone": telefone, "Vaga": vaga}
    clientes.append(cliente)
    pagamentos.append({"Nome": nome, "CPF": cpf, "Valor": valor_pagamento, "Forma de Pagamento": forma_pagamento, "Data": data_pagamento})
    vagas[vaga] = False

    cadastrar_carro(cliente, valor_pagamento, vaga)

def cadastrar_usuario():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()

    if not nome or not cpf or not email or not senha:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")
    cadastro_janela.destroy()

def abrir_cadastro_usuario():
    global cadastro_janela, nome_entry, cpf_entry, email_entry, senha_entry

    cadastro_janela = tk.Toplevel(janela)
    cadastro_janela.title("Cadastro de Usuário - Estaciona Fácil")
    cadastro_janela.geometry("400x600")
    cadastro_janela.configure(bg=cor_fundo)

    titulo = tk.Label(cadastro_janela, text="Cadastro de Usuário", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=20)

    nome_label = tk.Label(cadastro_janela, text="Nome:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    nome_label.pack(pady=5)
    nome_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    nome_entry.pack(padx=20, pady=5, fill="x")

    cpf_label = tk.Label(cadastro_janela, text="CPF:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    cpf_label.pack(pady=5)
    cpf_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    cpf_entry.pack(padx=20, pady=5, fill="x")

    email_label = tk.Label(cadastro_janela, text="E-mail:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    email_label.pack(pady=5)
    email_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    email_entry.pack(padx=20, pady=5, fill="x")

    senha_label = tk.Label(cadastro_janela, text="Senha:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    senha_label.pack(pady=5)
    senha_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto, show="*")
    senha_entry.pack(padx=20, pady=5, fill="x")

    cadastrar_btn = tk.Button(cadastro_janela, text="Cadastrar", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto, command=cadastrar_usuario)
    cadastrar_btn.pack(pady=20, padx=20, fill="x")

def abrir_cadastro_cliente():
    global cadastro_janela, nome_entry, cpf_entry, email_entry, telefone_entry, vaga_entry, tempo_entry, pagamento_var

    cadastro_janela = tk.Toplevel(janela)
    cadastro_janela.title("Cadastro de Cliente - Estaciona Fácil")
    cadastro_janela.geometry("350x650")
    cadastro_janela.configure(bg=cor_fundo)

    titulo = tk.Label(cadastro_janela, text="Cadastro de Cliente", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=20)

    nome_label = tk.Label(cadastro_janela, text="Nome:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    nome_label.pack(pady=5)
    nome_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    nome_entry.pack(padx=20, pady=5, fill="x")

    cpf_label = tk.Label(cadastro_janela, text="CPF:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    cpf_label.pack(pady=5)
    cpf_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    cpf_entry.pack(padx=20, pady=5, fill="x")

    email_label = tk.Label(cadastro_janela, text="E-mail:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    email_label.pack(pady=5)
    email_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    email_entry.pack(padx=20, pady=5, fill="x")

    telefone_label = tk.Label(cadastro_janela, text="Telefone:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    telefone_label.pack(pady=5)
    telefone_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    telefone_entry.pack(padx=20, pady=5, fill="x")

    vaga_label = tk.Label(cadastro_janela, text="Vaga:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    vaga_label.pack(pady=5)
    vaga_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    vaga_entry.pack(padx=20, pady=5, fill="x")

    tempo_label = tk.Label(cadastro_janela, text="Tempo (horas):", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    tempo_label.pack(pady=5)
    tempo_entry = tk.Entry(cadastro_janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    tempo_entry.pack(padx=20, pady=5, fill="x")

    pagamento_label = tk.Label(cadastro_janela, text="Forma de Pagamento:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
    pagamento_label.pack(pady=5)
    pagamento_var = tk.StringVar(cadastro_janela)
    pagamento_var.set("Dinheiro") 
    pagamento_menu = tk.OptionMenu(cadastro_janela, pagamento_var, "Dinheiro", "Cartão", "Pix")
    pagamento_menu.config(font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    pagamento_menu.pack(padx=20, pady=5, fill="x")

    cadastrar_btn = tk.Button(cadastro_janela, text="Cadastrar", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto, command=cadastrar_cliente)
    cadastrar_btn.pack(pady=20, padx=20, fill="x")

def visualizar_clientes():
    global clientes_janela, clientes_selecionado

    clientes_selecionado = None

    clientes_janela = tk.Toplevel(janela)
    clientes_janela.title("Clientes - Estaciona Fácil")
    clientes_janela.geometry("450x600")
    clientes_janela.configure(bg=cor_fundo)

    titulo = tk.Label(clientes_janela, text="Clientes Cadastrados", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=20)

    frame_externo = tk.Frame(clientes_janela, bg=cor_fundo)
    frame_externo.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_externo, bg=cor_fundo)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_externo, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_interno = tk.Frame(canvas, bg=cor_fundo)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    def selecionar_cliente(event):
        global clientes_selecionado
        widget = event.widget
        clientes_selecionado = widget.cget("text") 

    for cliente in clientes:
        texto = (f"Nome: {cliente['Nome']}\n"
                 f"CPF: {cliente['CPF']}\n"
                 f"E-mail: {cliente['Email']}\n"
                 f"Telefone: {cliente['Telefone']}\n"
                 f"Vaga Ocupada: {cliente['Vaga']}\n")

        if "Carro" in cliente:
            texto += (f"Modelo: {cliente['Carro']['Modelo']}\n"
                      f"Placa: {cliente['Carro']['Placa']}\n"
                      f"Cor: {cliente['Carro']['Cor']}\n")

        cliente_label = tk.Label(frame_interno, text=texto, font=fonte_texto, bg=cor_fundo, fg=cor_texto, anchor="w",
                                 justify="left", padx=10, pady=5, relief="groove",
                                 bd=1)  
        cliente_label.pack(pady=5, padx=10, fill="x")

        cliente_label.bind("<Button-1>", selecionar_cliente)

    excluir_btn = tk.Button(clientes_janela, text="Excluir", font=fonte_texto, bg="red", fg=cor_botao_texto,
                            command=excluir_cliente)
    excluir_btn.pack(pady=20, padx=20, fill="x")

    frame_interno.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def excluir_cliente():
    global clientes_selecionado
    if clientes_selecionado:
        for cliente in clientes:
            
            texto_cliente = f"Nome: {cliente['Nome']}\nCPF: {cliente['CPF']}\nE-mail: {cliente['Email']}\nTelefone: {cliente['Telefone']}\nVaga Ocupada: {cliente['Vaga']}\n"
            if "Carro" in cliente:
                texto_cliente += f"Modelo: {cliente['Carro']['Modelo']}\nPlaca: {cliente['Carro']['Placa']}\nCor: {cliente['Carro']['Cor']}\n"
            if texto_cliente == clientes_selecionado:
                clientes.remove(cliente)
                vagas[cliente['Vaga']] = True  
                messagebox.showinfo("Exclusão", f"Cliente {cliente['Nome']} foi excluído com sucesso!")
                visualizar_clientes()  
                return
    else:
        messagebox.showerror("Erro", "Nenhum cliente selecionado!")

def excluir_pagamento():
    global pagamento_selecionado
    if pagamento_selecionado:
        for pagamento in pagamentos:
            texto_pagamento = f"Nome: {pagamento['Nome']}\nCPF: {pagamento['CPF']}\nValor: R$ {pagamento['Valor']},00\nForma de Pagamento: {pagamento['Forma de Pagamento']}\nData: {pagamento['Data']}\n"
            if texto_pagamento == pagamento_selecionado:
                pagamentos.remove(pagamento)
                messagebox.showinfo("Exclusão", f"Pagamento de {pagamento['Nome']} foi excluído com sucesso!")
                visualizar_pagamentos() 
                return
    else:
        messagebox.showerror("Erro", "Nenhum pagamento selecionado!")

def visualizar_pagamentos():
    global pagamentos_janela, pagamento_selecionado

    pagamento_selecionado = None

    pagamentos_janela = tk.Toplevel(janela)
    pagamentos_janela.title("Pagamentos - Estaciona Fácil")
    pagamentos_janela.geometry("450x600")  
    pagamentos_janela.configure(bg=cor_fundo)

    titulo = tk.Label(pagamentos_janela, text="Pagamentos Realizados", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=20)

    frame_externo = tk.Frame(pagamentos_janela, bg=cor_fundo)
    frame_externo.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_externo, bg=cor_fundo)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_externo, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_interno = tk.Frame(canvas, bg=cor_fundo)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    def selecionar_pagamento(event):
        global pagamento_selecionado
        widget = event.pagamento_selecionado = widget.cget("text")  # Pega o texto do pagamento clicado

    for pagamento in pagamentos:
        texto = (f"Nome: {pagamento['Nome']}\n"
                 f"CPF: {pagamento['CPF']}\n"
                 f"Valor: R$ {pagamento['Valor']},00\n"
                 f"Forma de Pagamento: {pagamento['Forma de Pagamento']}\n"
                 f"Data: {pagamento['Data']}\n")
        pagamento_label = tk.Label(frame_interno, text=texto, font=fonte_texto, bg=cor_fundo, fg=cor_texto, anchor="w",
                                    justify="left", padx=10, pady=5, relief="groove",
                                    bd=1)  
        pagamento_label.pack(pady=5, padx=10, fill="x")

        pagamento_label.bind("<Button-1>", selecionar_pagamento)

    excluir_btn = tk.Button(pagamentos_janela, text="Excluir", font=fonte_texto, bg="red", fg=cor_botao_texto,
                            command=excluir_pagamento)
    excluir_btn.pack(pady=20, padx=20, fill="x")

    frame_interno.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def menu():
    menu_janela = tk.Toplevel(janela)
    menu_janela.title("Menu - Estaciona Fácil")
    menu_janela.geometry("400x400")
    menu_janela.configure(bg=cor_fundo)

    titulo = tk.Label(menu_janela, text="Menu", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=20)

    clientes_btn = tk.Button(menu_janela, text="Clientes", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto,
                              command=visualizar_clientes)
    clientes_btn.pack(pady=10, padx=20, fill="x")

    cadastrar_btn = tk.Button(menu_janela, text="Cadastrar Clientes", font=fonte_texto, bg=cor_botao,
                               fg=cor_botao_texto, command=abrir_cadastro_cliente)
    cadastrar_btn.pack(pady=10, padx=20, fill="x")

    vagas_btn = tk.Button(menu_janela, text="Vagas", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto,
                           command=visualizar_vagas)
    vagas_btn.pack(pady=10, padx=20, fill="x")

    pagamentos_btn = tk.Button(menu_janela, text="Pagamentos", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto,
                                command=visualizar_pagamentos)
    pagamentos_btn.pack(pady=10, padx=20, fill="x")

# Função para exibir o status das vagas
def visualizar_vagas():
    vagas_janela = tk.Toplevel(janela)
    vagas_janela.title("Vagas - Estaciona Fácil")
    vagas_janela.geometry("300x400")  # Ajuste a largura e altura conforme necessário
    vagas_janela.configure(bg=cor_fundo)

    titulo = tk.Label(vagas_janela, text="Status das Vagas", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=10)

    # Frame externo contendo Canvas e Scrollbar
    frame_externo = tk.Frame(vagas_janela, bg=cor_fundo)
    frame_externo.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_externo, bg=cor_fundo)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_externo, orient="vertical", command=canvas.yview)  # Scrollbar vertical
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)  # Configura o scroll vertical

    # Frame interno onde as vagas serão exibidas
    frame_interno = tk.Frame(canvas, bg=cor_fundo)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    # Adicionando informações das vagas em lista vertical
    for i in range(1, 33):
        status = "Disponível" if vagas[i] else "Ocupada"
        cor_texto_vaga = "green" if vagas[i] else "red"
        vaga_label = tk.Label(frame_interno, text=f"Vaga {i}: {status}", font=fonte_texto, bg="#ecf0f1",
                               fg=cor_texto_vaga, padx=10, pady=5, relief="groove")
        vaga_label.pack(fill="x")  # Organiza as vagas em lista vertical

    frame_interno.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
def login():
    email = email_entry.get()
    senha = senha_entry.get()

    if not email or not senha:
        messagebox.showwarning("Aviso", "Por favor, preencha o e-mail e a senha.")
    else:
        messagebox.showinfo("Login", "Login efetuado com sucesso!")
        janela.withdraw() 
        menu()

# Criação da janela principal
janela = tk.Tk()
janela.title("Estaciona Fácil")
janela.geometry("400x450")  
janela.configure(bg=cor_fundo)

# Tela de Login
titulo = tk.Label(janela, text="Estaciona Fácil", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
titulo.pack(pady=30)

subtitulo = tk.Label(janela, text="Login", font=fonte_subtitulo, bg=cor_fundo, fg=cor_texto)
subtitulo.pack(pady=15)

email_label = tk.Label(janela, text="E-mail:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
email_label.pack(pady=5)

email_entry = tk.Entry(janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
email_entry.pack(padx=20, pady=5, fill="x")

senha_label = tk.Label(janela, text="Senha:", font=fonte_texto, bg=cor_fundo, fg=cor_texto)
senha_label.pack(pady=5)
senha_entry = tk.Entry(janela, font=fonte_texto, bg="#ecf0f1", fg=cor_texto, show="*")
senha_entry.pack(padx=20, pady=5, fill="x")

login_btn = tk.Button(janela, text="Entrar", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto, command=login)
login_btn.pack(pady=20, padx=20, fill="x")

cadastro_btn = tk.Button(janela, text="Cadastrar-se", font=fonte_texto, bg=cor_botao, fg=cor_botao_texto,command=abrir_cadastro_usuario) 
cadastro_btn.pack(pady=10, padx=20, fill="x")
janela.mainloop()
