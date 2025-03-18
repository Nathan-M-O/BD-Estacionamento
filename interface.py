import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def configurar_tema():
    global cor_principal, cor_secundaria, cor_texto, cor_fundo, cor_botao, cor_botao_texto, fonte_titulo, fonte_subtitulo, fonte_texto
    cor_principal = "#2c3e50"
    cor_secundaria = "#3498db"
    cor_texto = "#333333"
    cor_fundo = "white"
    cor_botao = "#7f8c8d"
    cor_botao_texto = "white"
    fonte_titulo = ("Arial", 24, "bold")
    fonte_subtitulo = ("Arial", 18)
    fonte_texto = ("Arial", 12)

configurar_tema()

def criar_label(master, texto):
    return tk.Label(master, text=texto, font=fonte_texto, bg=cor_fundo, fg=cor_texto)

def criar_entry(master, mostrar=None):
    return tk.Entry(master, font=fonte_texto, bg="#ecf0f1", fg=cor_texto, show=mostrar)

def criar_botao(master, texto, comando, cor_bg=None):
    cor_bg = cor_bg or cor_botao
    return tk.Button(master, text=texto, font=fonte_texto, bg=cor_bg, fg=cor_botao_texto, command=comando)

# dados globais
clientes = []
pagamentos = []
usuarios = []
vagas = {i: True for i in range(1, 33)}

def cadastrar_usuario():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    senha = senha_entry.get()

    if not nome or not cpf or not email or not senha:
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        return

    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            messagebox.showerror("Erro", "Já existe um usuário com este CPF.")
            return

    usuarios.append({"Nome": nome, "CPF": cpf, "Email": email, "Senha": senha})
    messagebox.showinfo("Cadastro", f"Usuário {nome} cadastrado com sucesso!")
    cadastro_janela.destroy()

def abrir_cadastro_usuario():
    global cadastro_janela, nome_entry, cpf_entry, email_entry, senha_entry
    cadastro_janela = tk.Toplevel(janela)
    cadastro_janela.title("Cadastro de Usuário - Estaciona Fácil")
    cadastro_janela.geometry("400x450")
    cadastro_janela.configure(bg=cor_fundo)

    criar_label(cadastro_janela, "Cadastro de Usuário").pack(pady=20)
    criar_label(cadastro_janela, "Nome:").pack(pady=5)
    nome_entry = criar_entry(cadastro_janela)
    nome_entry.pack(pady=5, fill="x", padx=20)

    criar_label(cadastro_janela, "CPF:").pack(pady=5)
    cpf_entry = criar_entry(cadastro_janela)
    cpf_entry.pack(pady=5, fill="x", padx=20)

    criar_label(cadastro_janela, "E-mail:").pack(pady=5)
    email_entry = criar_entry(cadastro_janela)
    email_entry.pack(pady=5, fill="x", padx=20)

    criar_label(cadastro_janela, "Senha:").pack(pady=5)
    senha_entry = criar_entry(cadastro_janela, mostrar="*")
    senha_entry.pack(pady=5, fill="x", padx=20)

    criar_botao(cadastro_janela, "Cadastrar", cadastrar_usuario).pack(pady=20, padx=20, fill="x")

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
    pagamento_var.set("Dinheiro")  # Valor padrão
    pagamento_menu = tk.OptionMenu(cadastro_janela, pagamento_var, "Dinheiro", "Cartão", "Pix")
    pagamento_menu.config(font=fonte_texto, bg="#ecf0f1", fg=cor_texto)
    pagamento_menu.pack(padx=20, pady=5, fill="x")

def visualizar_vagas():
    vagas_janela = tk.Toplevel(janela)
    vagas_janela.title("Vagas - Estaciona Fácil")
    vagas_janela.geometry("300x400")
    vagas_janela.configure(bg=cor_fundo)

    titulo = tk.Label(vagas_janela, text="Status das Vagas", font=fonte_titulo, bg=cor_fundo, fg=cor_principal)
    titulo.pack(pady=10)

    frame_externo = tk.Frame(vagas_janela, bg=cor_fundo)
    frame_externo.pack(fill="both", expand=True, padx=10, pady=10)

    canvas = tk.Canvas(frame_externo, bg=cor_fundo)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(frame_externo, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_interno = tk.Frame(canvas, bg=cor_fundo)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")

    for i in range(1, 33):
        status = "Disponível" if vagas[i] else "Ocupada"
        cor_texto_vaga = "green" if vagas[i] else "red"
        vaga_label = tk.Label(frame_interno, text=f"Vaga {i}: {status}", font=fonte_texto, bg="#ecf0f1", fg=cor_texto_vaga, padx=10, pady=5, relief="groove")
        vaga_label.pack(fill="x")

    frame_interno.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# menu
def menu():
    menu_janela = tk.Toplevel(janela)
    menu_janela.title("Menu - Estaciona Fácil")
    menu_janela.geometry("400x400")
    menu_janela.configure(bg=cor_fundo)

    criar_label(menu_janela, "Menu").pack(pady=20)

    criar_botao(menu_janela, "Clientes", visualizar_clientes).pack(pady=10, padx=20, fill="x")
    criar_botao(menu_janela, "Cadastrar Cliente", abrir_cadastro_cliente).pack(pady=10, padx=20, fill="x")
    criar_botao(menu_janela, "Pagamentos", visualizar_pagamentos).pack(pady=10, padx=20, fill="x")
    criar_botao(menu_janela, "Vagas", visualizar_vagas).pack(pady=10, padx=20, fill="x")

    def visualizar_pagamentos():
     global pagamentos_janela, pagamento_selecionado

    pagamento_selecionado = None

    pagamentos_janela = tk.Toplevel(janela)
    pagamentos_janela.title("Pagamentos - Estaciona Fácil")
    pagamentos_janela.geometry("450x600")
    pagamentos_janela.configure(bg=cor_fundo)

    titulo = criar_label(pagamentos_janela, "Pagamentos Realizados")
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
        widget = event.widget
        pagamento_selecionado = widget.cget("text")  # captura o texto do widget selecionado

    for pagamento in pagamentos:
        texto = (f"Nome: {pagamento['Nome']}\n"
                 f"CPF: {pagamento['CPF']}\n"
                 f"Valor: R$ {pagamento['Valor']},00\n"
                 f"Forma de Pagamento: {pagamento['Forma de Pagamento']}\n"
                 f"Data: {pagamento['Data']}\n")
        pagamento_label = tk.Label(frame_interno, text=texto, font=fonte_texto, bg=cor_fundo, fg=cor_texto,
                                    anchor="w", justify="left", padx=10, pady=5, relief="groove", bd=1)
        pagamento_label.pack(pady=5, padx=10, fill="x")
        pagamento_label.bind("<Button-1>", selecionar_pagamento)  # adiciona o evento de clique

    excluir_btn = criar_botao(pagamentos_janela, "Excluir", excluir_pagamento, cor_bg="red")
    excluir_btn.pack(pady=20, padx=20, fill="x")

    frame_interno.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def excluir_pagamento():
    global pagamento_selecionado
    if pagamento_selecionado:
        for pagamento in pagamentos:
            texto_pagamento = (f"Nome: {pagamento['Nome']}\n"
                               f"CPF: {pagamento['CPF']}\n"
                               f"Valor: R$ {pagamento['Valor']},00\n"
                               f"Forma de Pagamento: {pagamento['Forma de Pagamento']}\n"
                               f"Data: {pagamento['Data']}\n")
            if texto_pagamento == pagamento_selecionado:
                pagamentos.remove(pagamento)  # remove o pagamento da lista
                messagebox.showinfo("Exclusão", f"Pagamento de {pagamento['Nome']} foi excluído com sucesso!")
                visualizar_pagamentos()  # atualiza a tela de pagamentos
                return
    else:
        messagebox.showerror("Erro", "Nenhum pagamento selecionado!")

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

# interface inicial
janela = tk.Tk()
janela.title("Estaciona Fácil")
janela.geometry("400x450")
janela.configure(bg=cor_fundo)

criar_label(janela, "Estaciona Fácil").pack(pady=30)
criar_label(janela, "Login").pack(pady=15)

criar_label(janela, "E-mail:").pack(pady=5)
email_entry = criar_entry(janela)
email_entry.pack(pady=5, fill="x", padx=20)

criar_label(janela, "Senha:").pack(pady=5)
senha_entry = criar_entry(janela, mostrar="*")
senha_entry.pack(pady=5, fill="x", padx=20)

criar_botao(janela, "Entrar", lambda: messagebox.showinfo("Login", "Login realizado!")).pack(pady=20, padx=20, fill="x")
criar_botao(janela, "Cadastrar-se", abrir_cadastro_usuario).pack(pady=10, padx=20, fill="x")

janela.mainloop()
