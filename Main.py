import time

import customtkinter as custom
from PIL import Image
import arena_7
import Dxd_gelo
import Dxd_trem


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

Definir configurações gerais para o macro funcionar:
Fechar janela do chat.
Visao: passaro
Desabilitar barra de hp monstro
Ativar barra de hp própria
3a Aba F1

DU: 
1a skill: cacador falcao
2a skill: chamas do infinito
3a skill: corte relampagado
4 skill: tempestade mortal
9a skill: esquiva
0 skill: desliza

'''


def main():
    # Janela inicial
    custom.set_appearance_mode("dark")
    janela = custom.CTk()
    janela.geometry("800x430")
    janela.title("Macro Cabal Online")
    janela.resizable(False, False)

    img = Image.open("img/login.png")
    side_img = custom.CTkImage(dark_image=img, light_image=img, size=(350, 430))
    label_img = custom.CTkLabel(janela, image=side_img, text="")
    label_img.place(x=0, y=0)
    texto = custom.CTkLabel(janela, text="Escolha sua dg", font=("Arial Bold", 24))
    texto.place(x=460, y=20)

    # dgs
    def escolher_dg(dg):
        if dg == 1:
            iniciar(1)
            # print("1")
        if dg == 2:
            iniciar(2)
            # print("2")
        if dg == 3:
            iniciar(3)

    botao1 = custom.CTkButton(janela, text="Arena 7", fg_color="#fc6603", hover_color="#fc4e03",
                              font=("Arial Bold", 13), text_color="#ffffff",
                              command=lambda: escolher_dg(1))
    botao1.place(x=370, y=100)

    botao2 = custom.CTkButton(janela, text="Dx desperta gelo", fg_color="#fc6603", hover_color="#fc4e03",
                              font=("Arial Bold", 13), text_color="#ffffff",
                              command=lambda: escolher_dg(2))
    botao2.place(x=370, y=140)

    botao3 = custom.CTkButton(janela, text="Dx desperta trem", fg_color="#fc6603", hover_color="#fc4e03",
                              font=("Arial Bold", 13), text_color="#ffffff",
                              command=lambda: escolher_dg(3))
    botao3.place(x=370, y=180)

    ########## Tentativa de incrementar console ###########
    # frame = custom.CTkFrame(master=janela, width=200, height=200, bg_color="#000000", border_width=1, border_color="#ffffff")
    # frame.place(x=580, y=210)
    # console_text = custom.StringVar()
    # console = custom.CTkLabel(master=frame, anchor='nw', bg_color="#000000", height=194, width=193, textvariable=console_text, text_color="#fc6603",
    #                    font=("Arial bold", 12))
    # console.place(x=3,y=3)
    #######################################################

    janela.mainloop()


def iniciar(dg):
    i = 0
    if dg == 1:
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title="Arena 7", font=("Roboto", 15))
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError:
            new_window = custom.CTkToplevel()
            new_window.title("Erro")
            new_window.geometry("395x100")

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Roboto", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            print("Valor inválido.")
            raise Exception("Valor invalido")

        print("###################### INICIANDO ##################################")
        print(f"Número de entradas: {numero_entradas}")
        time.sleep(3)
        while i < numero_entradas:
            arena_7.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                print(f"###################### RESTAM {restante} ENTRADAS ##################################")
            else:
                print(f"###################### TODAS AS ENTRADAS FINALIZADAS ##################################")
            i += 1

    if dg == 2:
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title="Dx desperta GELO",
                                                 font=("Roboto", 15))
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError:
            new_window = custom.CTkToplevel()
            new_window.title("Erro")
            new_window.geometry("395x100")

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Roboto", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            print("Valor inválido.")
            raise Exception("Valor invalido")
        print("###################### INICIANDO ##################################")
        print(f"Número de entradas: {numero_entradas}")
        time.sleep(3)
        while i < numero_entradas:
            Dxd_gelo.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                print(f"###################### RESTAM {restante} ENTRADAS ##################################")
            else:
                print(f"###################### TODAS AS ENTRADAS FINALIZADAS ##################################")
            i += 1

    if dg == 3:
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title="Dx desperta TREM",
                                                 font=("Roboto", 15))
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError:
            new_window = custom.CTkToplevel()
            new_window.title("Erro")
            new_window.geometry("395x100")

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Roboto", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            print("Valor inválido.")
            raise Exception("Valor invalido")
 #Colocar log       # with open('test.txt', 'w') as f:
        #     print("###################### INICIANDO ##################################", file=f)
        print("###################### INICIANDO ##################################")
        print(f"Número de entradas: {numero_entradas}")
        time.sleep(3)
        while i < numero_entradas:
            print(f"DG número: {i + 1}")
            Dxd_trem.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                print(f"###################### RESTAM {restante} ENTRADAS ##################################")
            else:
                print(f"###################### TODAS AS ENTRADAS FINALIZADAS ##################################")
            i += 1


main()
