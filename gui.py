import tkinter as tk
from tkinter import tkinte

class PrincipalBD:
    def __init_(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gestão de Produtos")

        # components da interface fráfica
        self.lblCodigo = tk.label(root, text="Código")
        self.lblCodigo.grid(row=0, column=0)
        self.textCodigo = tk.Entry(root)
        self.txtCodigo.grid(row=0, column=1)

        self.lblNome = tk.label(root, text="Nome")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblPreco = tk.label(root, text="Preço")
        self.lblPreco.grid(row=2, column=0)
        self.textPreco = tk.Entry(root)
        self.txtCPreco.grid(row=2, column=1)

        self.btnCadastrar = tk.Button(root, text="Cadastrar", command=self.fCadastrarProduto)
        self.btnCadastrar.grid(row=3, column=0)

        self.btnCadastrar = tk.Button(root, text="Atualizar", command=self.fAtualizarProduto)
        self.btnCadastrar.grid(row=3, column=1)

        self.btnCadastrar = tk.Button(root, text="Excluir", command=self.fExcluirProduto)
        self.btnCadastrar.grid(row=4, column=0)

        self.btnCadastrar = tk.Button(root, text="Limpar", command=self.fLimparTela)
        self.btnCadastrar.grid(row=4, column=1)

        self.tree = ttk.Treview(root, columns=("CODIGO", "NOME", "PRECO"), show="headings")
        self.tree.headings("CODIGO", text="Código")
        self.tree.headings("NOME", text="Nome")
        self.tree.headings("PRECO", text="Preço")

        sef.tree.grid(row=5, column=0, columnspan=2)

        self.carregaDadosIniciais()


    def fCadastrarProduto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()

        self.db.inserir_dados(nome, preco)
        self.tree.insert("", "end", values=(codigo, nome, preco))
        self.fLimparTela()


    def fAtualizarProduto(self):
        digo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        self.db.atualizar_dados(codigo, nome, preco)
        self.fLimparTela()
        self.carregaDadosIniciais()

    def fExcluirProduto(self):
        codigo = self.txtCodigo.get()
        self.db.excluir_dados(codigo)
        self.fLimparTela()
        self.carregaDadosIniciais()


    def fLimparTela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txt.delete(0, tk.END)

    def apresentarRegistrosSelecionados(self, event):

        item = self.tree.selection()[0]
        valores = self.tree.item(item, "values")

        self.txtCodigo.delete(0, tk.END)
        self.txtCodigo.insert(tk.END, valores[0])

        
        self.txtNome.delete(0, tk.END)
        self.txtNome.insert(tk.END, valores[1])

        self.txtPreco.delete(0, tk.END)
        self.txtPreco.insert(tk.END, valores[2])

    def carregarDadosIniciais(self): 
        for item in self.tree.get_children():
            self.tree.delete(item)

        registros = self.db.selecionar_dados()

        for registro in registros:
            self.tree.insert("", "end", values=registro)


# criando a interface gráfica
root = tk.tk()
app_bd= AppBD()
app_gui = PrincipalBD(root, app_bd)
root.mainloop()
