import tkinter as tk
from ui import InterfaceUI

def main():
    root = tk.Tk()
    root.title("Estaciona Fácil")
    root.geometry("400x450")

    ui = InterfaceUI(root)

    tk.Label(root, text="Estaciona Fácil", font=("Helvetica", 24, "bold")).pack(pady=20)
    tk.Button(root, text="Cadastrar Cliente", command=ui.abrir_cadastro_cliente).pack(pady=10)
    tk.Button(root, text="Visualizar Clientes", command=ui.visualizar_clientes).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
