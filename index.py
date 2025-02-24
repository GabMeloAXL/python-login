# Importar as bibliotecas necessárias
from tkinter import *
from tkinter import messagebox  # Para possíveis mensagens pop-up no futuro
from tkinter import ttk  # Para widgets temáticos
import DataBaser

# Criar a janela principal
jan = Tk()
jan.title("DP Systems - Painel de Acesso")  # Definir o título da janela
jan.geometry("600x300")  # Definir o tamanho da janela
jan.configure(background="white")  # Definir a cor de fundo da janela
jan.resizable(width=False, height=False)  # Desabilitar o redimensionamento da janela
jan.iconbitmap(default="icons/LogoIcon.ico")  # Definir o ícone da janela (se o arquivo existir)

# Carregar a imagem do logo
logo = PhotoImage(file="icons/logo.png")  # Carregar a imagem do logo (se o arquivo existir)

# Criar frames para dividir a janela
Leftframe = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
Leftframe.pack(side=LEFT)  # Posicionar o frame à esquerda
Rightframe = Frame(jan, width=365, height=300, bg="MIDNIGHTBLUE", relief="raise")
Rightframe.pack(side=RIGHT)  # Posicionar o frame à direita

# Exibir o logo no frame esquerdo
logoLabel = Label(Leftframe, image=logo, bg="MIDNIGHTBLUE")
logoLabel.place(x=50, y=100)  # Posicionar o logo

# Criar o rótulo de nome de usuário
userLabel = Label(Rightframe, text="Username:", font=("Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
userLabel.place(x=5, y=100)  # Posicionar o rótulo de nome de usuário

# Criar o campo de entrada para o nome de usuário
UserEntry = ttk.Entry(Rightframe, width=30)
UserEntry.place(x=150, y=105)  # Posicionar o campo de entrada de nome de usuário

# Criar o rótulo de senha
PassLabel = Label(Rightframe, text="Password:", font=("Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)  # Posicionar o rótulo de senha

# Criar o campo de entrada para a senha com máscara de senha
PassEntry = ttk.Entry(Rightframe, width=30, show="*")
PassEntry.place(x=150, y=155)  # Posicionar o campo de entrada de senha

# Criar o botão de login
LoginButton = ttk.Button(Rightframe, text="Login", width=20)
LoginButton.place(x=150, y=200)  # Posicionar o botão de login


# Criar uma função para registro (atualmente não funcional)
def Register():
    # Mover os botões existentes para fora da tela (solução temporária)
    LoginButton.place(x=5000)
    CriarCntButton.place(x=5000)

    # Criar widgets de registro (placeholders, funcionalidade não implementada)
    NomeLabel = Label(Rightframe, text="Nome:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(Rightframe, width=31)
    NomeEntry.place(x=150, y=15)

    EmailLabel = Label(Rightframe, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(Rightframe, width=31)
    EmailEntry.place(x=150, y=65)

    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        DataBaser.cursor.execute("""
         INSERT INTO Users(Name, Email, User, Password)                        """)

    Registrar = ttk.Button(Rightframe, text="Registrar", width=20, command=RegisterToDataBase)
    Registrar.place(x=150, y=230)

    # Criar uma função para voltar à tela de login (placeholder, funcionalidade não implementada)
    def Backtologin():
        # Mover os widgets de registro para fora da tela (solução temporária)
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Registrar.place(x=5000)
        Back.place(x=5000)

        # Reposicionar os botões de login e criar conta
        LoginButton.place(x=150)
        CriarCntButton.place(x=150)

    # Criar o botão de voltar
    Back = ttk.Button(Rightframe, text="Voltar", width=20, command=Backtologin)
    Back.place(x=150, y=200)


# Criar o botão de criar conta
CriarCntButton = ttk.Button(Rightframe, text="Criar conta", width=20, command=Register)
CriarCntButton.place(x=150, y=230)

# Iniciar o loop principal da interface gráfica
jan.mainloop()