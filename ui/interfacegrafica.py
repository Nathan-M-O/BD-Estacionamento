import tkinter as tk
from tkinter import messagebox
from models import ClienteDAO

class InterfaceUI:
    def __init__(self, root):
        self.root = root
        self.cliente_dao = ClienteDAO()

    def abrir_cadastro_cliente(self):
        cadastro_janela = tk.Toplevel(self.root)
        cadastro_janela.title("Cadastro de Cliente")
        cadastro_janela.geometry("400x400")

        tk.Label(cadastro_janela, text="Nome").pack()
        nome_entry = tk.Entry(cadastro_janela)
        nome_entry.pack()

        tk.Label(cadastro_janela, text="CPF").pack()
        cpf_entry = tk.Entry(cadastro_janela)
        cpf_entry.pack()

        tk.Label(cadastro_janela, text="Telefone").pack()
        telefone_entry = tk.Entry(cadastro_janela)
        telefone_entry.pack()

        tk.Label(cadastro_janela, text="E-mail").pack()
        email_entry = tk.Entry(cadastro_janela)
        email_entry.pack()

        def cadastrar_cliente():
            nome = nome_entry.get()
            cpf = cpf_entry.get()
            telefone = telefone_entry.get()
            email = email_entry.get()
            if self.cliente_dao.cadastrar((nome, cpf, telefone, email)):
                messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
                cadastro_janela.destroy()
            else:
                messagebox.showerror("Erro", "Erro ao cadastrar cliente no banco de dados.")

        tk.Button(cadastro_janela, text="Cadastrar", command=cadastrar_cliente).pack(pady=20)

    def visualizar_clientes(self):
        clientes = self.cliente_dao.listar()

        clientes_janela = tk.Toplevel(self.root)
        clientes_janela.title("Clientes")
        clientes_janela.geometry("500x400")

        for cliente in clientes:
            texto = f"ID: {cliente['cod_cliente']} | Nome: {cliente['nome']} | CPF: {cliente['cpf']}"
            tk.Label(clientes_janela, text=texto, anchor="w").pack(fill="x")
