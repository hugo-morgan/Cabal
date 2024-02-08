import customtkinter as custom
import Dxd_fogo
import Dxd_gelo

def center(win):
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
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    win.deiconify()
'''

Definir configurações gerais para o macro funcionar, como tamanho de letra,
fonte, tipo de câmera, etc.
Visao: passaro
DU: 
1a skill: cacador falcao
2a skill: chamas do infinito
3a skill: corte relampagado
4 skill: tempestade mortal

'''


def iniciar(dg):
    if dg == 1:
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title="Dx desperta FOGO", font=("Roboto", 15))
        numero_entradas = quantas_entradas.get_input()
        try:
            x = int(numero_entradas)
            Dxd_fogo.play(int(numero_entradas))
        except:
            new_window = custom.CTkToplevel()
            new_window.title("Erro")
            new_window.geometry("395x100")
            print("Valor inválido.")

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Roboto", 15))
            text.place(x=40, y=20)

            ok = custom.CTkButton(new_window, text="Ok", command=lambda:new_window.destroy())
            ok.place(x=120,y=60)

    if dg == 2:
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title="Dx desperta GELO", font=("Roboto", 15))
        numero_entradas = quantas_entradas.get_input()
        try:
            x = int(numero_entradas)
            Dxd_gelo.play(int(numero_entradas))
        except:
            new_window = custom.CTkToplevel()
            new_window.title("Erro")
            new_window.geometry("400x100")
            print("Valor inválido.")

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Roboto", 15))
            text.place(x=40, y=20)

            ok = custom.CTkButton(new_window, text="Ok", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)

def main():
# Janela inicial
    custom.set_appearance_mode("dark")
    janela = custom.CTk()
    janela.geometry("500x400")
    janela.title("Macro Cabal Online")
    janela.resizable(False, False)

    frame = custom.CTkFrame(janela, width=200, height=396)
    frame.grid(padx=0, pady=0)

    texto = custom.CTkLabel(frame, text="Escolha sua dg", font=("Roboto", 25))
    texto.place(x=10, y=150)
    # dgs
    def escolher_dg(dg):
        if dg == 1:
            iniciar(1)
            # print("1")
        if dg == 2:
            iniciar(2)
            # print("2")

    botao1 = custom.CTkButton(janela, text="dxd fogo", fg_color="red", font=("Roboto", 12, "bold"), command=lambda:escolher_dg(1))
    botao1.place(x= 210, y = 15)

    botao2 = custom.CTkButton(janela, text="dxd gelo", fg_color="green", font=("Arial", 12, "bold"), command=lambda:escolher_dg(2))
    botao2.place(x= 210, y=55)

    janela.mainloop()
