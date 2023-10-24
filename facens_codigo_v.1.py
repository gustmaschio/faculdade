import sqlite3
from tkinter import *
from tkinter import messagebox

# Conexão com o banco de dados de produtos
conn_produtos = sqlite3.connect("cadastro_produto.db")
cursor_produtos = conn_produtos.cursor()

cursor_produtos.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        codigo TEXT NOT NULL
    )
''')
conn_produtos.commit()

# Conexão com o banco de dados de usuários
conn_usuarios = sqlite3.connect("cadastro_usuarios.db")
cursor_usuarios = conn_usuarios.cursor()

cursor_usuarios.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn_usuarios.commit()

# Conexão com o banco de dados de arduino
conn_arduino = sqlite3.connect("cadastro_arduino.db")
cursor_arduino = conn_arduino.cursor()

cursor_arduino.execute('''
    CREATE TABLE IF NOT EXISTS arduino (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        arduino TEXT NOT NULL,
        digitar TEXT NOT NULL
    )
''')
conn_arduino.commit()


def listar_produtos():
    cursor_produtos.execute("SELECT * FROM produtos ORDER BY id")
    produtos = cursor_produtos.fetchall()
    for produto in produtos:
        print(produto)

def cadastrar_produto():
    nome = vnome.get()
    codigo = vcodigo.get()

    if nome and codigo:  # Verifica se ambos os campos estão preenchidos
        cursor_produtos.execute("INSERT INTO produtos (nome, codigo) VALUES (?, ?)", (nome, codigo))
        conn_produtos.commit()
        vnome.delete(0, END)
        vcodigo.delete(0, END)
        print("Produto cadastrado:", nome, codigo)
        listar_produtos()
    else:
        messagebox.showerror("Mensagem de Erro", "Você não digitou todos os campos!")

def cadastrar_novo_usuario():
    usuario = vusuario.get()
    email = vemail.get()

    if usuario and email:  # Verifica se ambos os campos estão preenchidos
        cursor_usuarios.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (usuario, email))
        conn_usuarios.commit()
        vusuario.delete(0, END)
        vemail.delete(0, END)
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def abrir_janela_cadastro_usuario():
    janela_cadastro_usuario = Toplevel(janela)
    janela_cadastro_usuario.title("Cadastro de Usuário")
    janela_cadastro_usuario.geometry("400x200")

    Label(janela_cadastro_usuario, text="Usuário:").grid(column=0, row=0)
    global vusuario
    vusuario = Entry(janela_cadastro_usuario)
    vusuario.grid(column=1, row=0)

    Label(janela_cadastro_usuario, text="E-mail:").grid(column=0, row=1)
    global vemail
    vemail = Entry(janela_cadastro_usuario)
    vemail.grid(column=1, row=1)

    Button(janela_cadastro_usuario, text="Cadastrar", command=cadastrar_novo_usuario).grid(column=0, row=2, columnspan=2)


def abrir_requisitos_arduino():
    arduino = varduino.get()
    digitar = vdigitar.get()

    if arduino and digitar:  # Verifica se ambos os campos estão preenchidos
        cursor_arduino.execute("INSERT INTO arduino (arduino, digitar) VALUES (?, ?)", (arduino, digitar))
        conn_arduino.commit()
        varduino.delete(0, END)
        vdigitar.delete(0, END)
        messagebox.showinfo("Cadastro", "Material necessário cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")

def abrir_janela_cadastro_arduino():
    janela_cadastro_arduino = Toplevel(janela)
    janela_cadastro_arduino.title("Requisitos de Arduino")
    janela_cadastro_arduino.geometry("400x200")

    Label(janela_cadastro_arduino, text="Material necessário:").grid(column=0, row=0)
    global varduino
    varduino = Entry(janela_cadastro_arduino)
    varduino.grid(column=1, row=0)

    Label(janela_cadastro_arduino, text="Quantidade:").grid(column=0, row=1)
    global vdigitar
    vdigitar = Entry(janela_cadastro_arduino)
    vdigitar.grid(column=1, row=1)

    Button(janela_cadastro_arduino, text="Cadastrar", command=abrir_requisitos_arduino).grid(column=0, row=2, columnspan=2)


    # Ação que deve ser executada ao clicar no botão "Requisitos do Arduino"
    pass

def sair():
    janela.quit()

janela = Tk()
janela.title("Cadastro de Produtos")
janela.geometry("400x200")

texto_orientacao = Label(janela, text="Digite o código e a descrição do produto para cadastro:")
texto_orientacao.grid(column=0, row=0, columnspan=2)

Label(janela, text="Por favor digite o código:").grid(column=0, row=1)
vnome = Entry(janela)
vnome.grid(column=1, row=1)

Label(janela, text="Por favor digite descrição do produto:").grid(column=0, row=2)
vcodigo = Entry(janela)
vcodigo.grid(column=1, row=2)

Button3 = Button(janela, text="Cadastrar", command=cadastrar_produto)
Button3.grid(column=0, row=3, columnspan=2)

Button4 = Button(janela, text="Cadastrar Usuário", command=abrir_janela_cadastro_usuario)
Button4.grid(column=0, row=4, columnspan=2)

Button6 = Button(janela, text="Requisitos do Arduino", command=abrir_janela_cadastro_arduino)
Button6.grid(column=0, row=5, columnspan=2)

Button5 = Button(janela, text="Sair", command=sair)
Button5.grid(column=0, row=6, columnspan=2)

listar_produtos()
janela.mainloop()