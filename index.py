#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Criar nossa janela
jan = Tk()
jan.title("DP Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="icons/LogoIcon.ico")

#===========    carregando logo
logo = PhotoImage(file="icons/logo.png")

#Widgets


#Dividir a janela 
Leftframe = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
Leftframe.pack(side=LEFT)
Rightframe = Frame(jan, width=365, height=300, bg="MIDNIGHTBLUE", relief="raise")
Rightframe.pack(side=RIGHT)

#########   definindo local do logo
logoLabel = Label(Leftframe, image=logo, bg="MIDNIGHTBLUE")
logoLabel.place(x=50, y=100)

#########   criando e definindo local da Label de username
userLabel = Label(Rightframe, text="Username:", font=("Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
userLabel.place(x=5, y=100) 

#########   criando e definindo local da entrada de username
UserEntry = ttk.Entry(Rightframe, width=30)
UserEntry.place(x=150, y=105)

#########   criando e definindo local da Label de Password

PassLabel = Label(Rightframe, text="Password:", font=("Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

#########   criando e definindo local da entrada de Password
PassEntry = ttk.Entry(Rightframe, width=30, show="*")
PassEntry.place(x=150, y=155)


## botoes

LoginButton = ttk.Button(Rightframe, text="Login", width=20)
LoginButton.place(x=150, y=200)


########Função Register

def Register():
    LoginButton.place(x=5000)
    CriarCntButton.place(x=5000)
    ####inserindo widgets de cadastro
    NomeLabel = Label(Rightframe, text="Nome:",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry = Entry(Rightframe, width=31)
    NomeEntry.place(x=150, y=15)

    EmailLabel = Label(Rightframe, text="Email:", font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5, y=55)

    EmailEntry = Entry(Rightframe, width=31)
    EmailEntry.place(x=150, y=65)

    Registrar = ttk.Button(Rightframe, text="Registrar", width=20)
    Registrar.place(x=150, y=230)

    def Backtologin():
        ####Removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)

        Registrar.place(x=5000)
        Back.place(x=5000)
        
        
        LoginButton.place(x=150)
        CriarCntButton.place(x=150)




    Back = ttk.Button(Rightframe, text="Voltar", width=20, command=Backtologin)
    Back.place(x=150, y=200)


CriarCntButton = ttk.Button(Rightframe, text="Criar conta", width=20, command=Register)
CriarCntButton.place(x=150, y=230)
jan.mainloop()