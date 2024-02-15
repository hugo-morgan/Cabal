import warnings
import customtkinter as custom
from tkinter import *
import mysql.connector
import sys
import os
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
def posicionar(win, x=0, y=0):
    # :param win: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    win.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    if x == 0 and y == 0:
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        x = x - 120
        y = y - 20
    else:
        x = x
        y = y

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='x',
    database='cabal'
)
print("Conexão bem sucedida!")
cursor = conexao.cursor()

f = ("Arial bold", 14)

janela = custom.CTk()
posicionar(janela)
janela.geometry("700x300")
janela.title("Login")
janela.resizable(False, False)

# FILTRO DE AVISO
warnings.filterwarnings("ignore")
# Background
img = PhotoImage(file=resource_path("img/login.png"))
img = img.zoom(35, 20)
img = img.subsample(70, 40)
label_img = custom.CTkLabel(janela, image=img, text="")
label_img.place(x=0, y=0)
# FILTRO DE AVISO
warnings.filterwarnings("always")

# frame
frame = custom.CTkFrame(janela, width=350, height=300)
frame.pack(side=RIGHT)

# Sistema
text = custom.CTkLabel(frame, text="Sistema de login", font=("Arial bold", 20))
text.place(x=100, y=20)

# id
login1 = custom.CTkLabel(frame, text="Login:", font=f)
login1.place(x=50, y=70)
login2 = custom.CTkEntry(frame, border_color="#fc6603", border_width=1, width=170, placeholder_text="Insira aqui seu usuário")
login2.place(x=100, y=70)
login = login2.get()

# senha
senha1 = custom.CTkLabel(frame, text="Senha:", font=f)
senha1.place(x=48, y=130)
senha2 = custom.CTkEntry(frame, border_color="#fc6603", border_width=1, width=170, placeholder_text="Insira aqui sua senha", show="*")
senha2.place(x=100, y=130)
senha = senha2.get()

def get_login(usuario):
    comando = f"""SELECT * FROM logins
    where usuario = '{usuario}'
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    login = resultado[0][1].lower()
    senha = resultado[0][2]
    return login, senha

def entrar():
    login = login2.get().lower()
    senha = senha2.get()
    print(f"login: {login} Senha: {senha}")
    # Condicao de login
    condicao = custom.StringVar()
    erro = custom.CTkLabel(master=frame, height=10, width=170, textvariable=condicao, text_color="red", font=("Arial bold", 12))
    erro.place(x=30, y=170)
    try:
        login, correta = get_login(login)
        if senha != correta:
            condicao.set("Senha incorreta.")
        elif senha == correta:
            janela.after(250, janela.destroy())
            import Main
    except:
        condicao.set("Usuario não existe.")

# entrar
entrar = custom.CTkButton(frame, text="Entrar", fg_color="#fc6603", hover_color="#fc4e03", font=("Arial Bold", 12), text_color="#ffffff", command=entrar)
entrar.place(x=110, y=200)

janela.mainloop()
cursor.close()
conexao.close()