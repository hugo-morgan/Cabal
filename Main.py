import time
import keyboard as kb
import customtkinter as custom
from PIL import Image

import arena_5
import arena_7
import Dxd_gelo
import Dxd_trem
import arena_6

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


'''

Definir configurações gerais para o macro funcionar:
Fechar janela do chat.
Visao: passaro
Botao home: selecionar personagem proprio
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

def iniciar(dg):
    i = 0
    console.delete("0.0", "end")
    if dg == "Arena 7":
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title=dg,
                                                 font=("Arial Bold", 15), button_hover_color="#fc6603", button_fg_color="#fc6603")
        posicionar(quantas_entradas, 80, 170)
        quantas_entradas.geometry("400x150")
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError or TypeError:
            new_window = custom.CTkToplevel()
            posicionar(new_window)
            new_window.title("Erro")
            new_window.geometry("395x100")
            new_window.wait_visibility()
            new_window.grab_set()

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Arial Bold", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            texto = ("\nValor inválido.")
            console.insert("end", texto)
            console.see("end")
            raise Exception("Valor invalido")

        texto = ("\n##### INICIANDO #####" +
                 "\n" + "Número de entradas: {}".format(numero_entradas)).ljust(50)
        console.insert("end", texto)
        console.see("end")

        time.sleep(3)
        while i < numero_entradas:
            if kb.is_pressed('end'):
                i = 10000
            texto = ("\nDG número: {}").format(i + 1)
            console.insert("end", texto)
            console.see("end")

            arena_7.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                texto = "\nRestam {} entradas".format(restante)
                console.insert("end", texto)
                console.see("end")
            else:
                texto = "\nTODAS AS ENTRADAS FINALIZADAS\n###########"
                console.insert("end", texto)
                console.see("end")

                entradas_finalizadas = custom.CTkToplevel()
                posicionar(entradas_finalizadas)
                entradas_finalizadas.title("Sucesso")
                entradas_finalizadas.geometry("375x100")
                entradas_finalizadas.wait_visibility()
                entradas_finalizadas.grab_set()


                text = custom.CTkLabel(entradas_finalizadas, text="Todas as entradas foram finalizadas.",
                                       font=("Arial Bold", 15))
                text.place(x=60, y=20)
                continuar = custom.CTkButton(entradas_finalizadas, font=("Arial bold", 13), fg_color="#fc6603",
                                             hover_color="#fc6603", text="Continuar",
                                             command=lambda: entradas_finalizadas.destroy())
                continuar.place(x=120, y=60)

                janela.focus_force()
            i += 1
###############################################################################################################################
    if dg == "Dx desperta gelo":
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title=dg,
                                                 font=("Arial Bold", 15), button_hover_color="#fc6603", button_fg_color="#fc6603")
        posicionar(quantas_entradas, 80, 170)
        quantas_entradas.geometry("400x150")
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError or TypeError:
            new_window = custom.CTkToplevel()
            posicionar(new_window)
            new_window.title("Erro")
            new_window.geometry("395x100")
            new_window.wait_visibility()
            new_window.grab_set()

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Arial Bold", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            texto = ("\nValor inválido.")
            console.insert("end", texto)
            console.see("end")
            raise Exception("Valor invalido")

        texto = ("\n##### INICIANDO #####" +
                 "\n" + "Número de entradas: {}".format(numero_entradas)).ljust(50)
        console.insert("end", texto)
        console.see("end")

        time.sleep(3)
        while i < numero_entradas:
            if kb.is_pressed('end'):
                i = 10000

            texto = ("\nDG número: {}").format(i + 1)
            console.insert("end", texto)
            console.see("end")

            Dxd_gelo.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                texto = "\nRestam {} entradas".format(restante)
                console.insert("end", texto)
                console.see("end")
            else:
                texto = "\nTODAS AS ENTRADAS FINALIZADAS\n###########"
                console.insert("end", texto)
                console.see("end")

                entradas_finalizadas = custom.CTkToplevel()
                posicionar(entradas_finalizadas)
                entradas_finalizadas.title("Sucesso")
                entradas_finalizadas.geometry("375x100")
                entradas_finalizadas.wait_visibility()
                entradas_finalizadas.grab_set()

                text = custom.CTkLabel(entradas_finalizadas, text="Todas as entradas foram finalizadas.",
                                       font=("Arial Bold", 15))
                text.place(x=60, y=20)
                continuar = custom.CTkButton(entradas_finalizadas, font=("Arial bold", 13), fg_color="#fc6603",
                                             hover_color="#fc6603", text="Continuar",
                                             command=lambda: entradas_finalizadas.destroy())
                continuar.place(x=120, y=60)
                janela.focus_force()
            i += 1
#################################################################################################################################
    if dg == "Dx desperta trem":
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title=dg,
                                                 font=("Arial Bold", 15), button_hover_color="#fc6603", button_fg_color="#fc6603")
        posicionar(quantas_entradas, 80, 170)
        quantas_entradas.geometry("400x150")
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError or TypeError:
            new_window = custom.CTkToplevel()
            posicionar(new_window)
            new_window.title("Erro")
            new_window.geometry("395x100")
            new_window.wait_visibility()
            new_window.grab_set()

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Arial Bold", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            texto = ("\nValor inválido.")
            console.insert("end", texto)
            console.see("end")
            raise Exception("Valor invalido")

        texto = ("\n##### INICIANDO #####" +
                 "\n" + "Número de entradas: {}".format(numero_entradas)).ljust(50)
        console.insert("end", texto)
        console.see("end")

        time.sleep(3)
        while i < numero_entradas:
            if kb.is_pressed('end'):
                i = 10000

            texto = ("\nDG número: {}").format(i + 1)
            console.insert("end", texto)
            console.see("end")

            Dxd_trem.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                texto = "\nRestam {} entradas".format(restante)
                console.insert("end", texto)
                console.see("end")
            else:
                texto = "\nTODAS AS ENTRADAS FINALIZADAS\n###########"
                console.insert("end", texto)
                console.see("end")

                entradas_finalizadas = custom.CTkToplevel()
                posicionar(entradas_finalizadas)
                entradas_finalizadas.title("Sucesso")
                entradas_finalizadas.geometry("375x100")
                entradas_finalizadas.wait_visibility()
                entradas_finalizadas.grab_set()

                text = custom.CTkLabel(entradas_finalizadas, text="Todas as entradas foram finalizadas.",
                                       font=("Arial Bold", 15))
                text.place(x=60, y=20)
                continuar = custom.CTkButton(entradas_finalizadas, font=("Arial bold", 13), fg_color="#fc6603",
                                             hover_color="#fc6603", text="Continuar",
                                             command=lambda: entradas_finalizadas.destroy())
                continuar.place(x=120, y=60)
                janela.focus_force()
            i += 1
###################################################################################################################################
    if dg == "Arena 6":
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title=dg,
                                                 font=("Arial Bold", 15), button_hover_color="#fc6603", button_fg_color="#fc6603")
        posicionar(quantas_entradas, 80, 170)
        quantas_entradas.geometry("400x150")
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError or TypeError:
            new_window = custom.CTkToplevel()
            posicionar(new_window)
            new_window.title("Erro")
            new_window.geometry("395x100")
            new_window.wait_visibility()
            new_window.grab_set()

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Arial Bold", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            texto = ("\nValor inválido.")
            console.insert("end", texto)
            console.see("end")
            raise Exception("Valor invalido")

        texto = ("\n##### INICIANDO #####" +
                 "\n" + "Número de entradas: {}".format(numero_entradas)).ljust(50)
        console.insert("end", texto)
        console.see("end")

        time.sleep(3)
        while i < numero_entradas:
            if kb.is_pressed('end'):
                i = 10000

            texto = ("\nDG número: {}").format(i + 1)
            console.insert("end", texto)
            console.see("end")

            arena_6.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                texto = "\nRestam {} entradas".format(restante)
                console.insert("end", texto)
                console.see("end")
            else:
                texto = "\nTODAS AS ENTRADAS FINALIZADAS\n###########"
                console.insert("end", texto)
                console.see("end")

                entradas_finalizadas = custom.CTkToplevel()
                posicionar(entradas_finalizadas)
                entradas_finalizadas.title("Sucesso")
                entradas_finalizadas.geometry("375x100")
                entradas_finalizadas.wait_visibility()
                entradas_finalizadas.grab_set()

                text = custom.CTkLabel(entradas_finalizadas, text="Todas as entradas foram finalizadas.",
                                       font=("Arial Bold", 15))
                text.place(x=60, y=20)
                continuar = custom.CTkButton(entradas_finalizadas, font=("Arial bold", 13), fg_color="#fc6603",
                                             hover_color="#fc6603", text="Continuar",
                                             command=lambda: entradas_finalizadas.destroy())
                continuar.place(x=120, y=60)
                janela.focus_force()
            i += 1
#################################################################################################################
    if dg == "Dx desperta fogo":
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title=dg,
                                                 font=("Arial Bold", 15), button_hover_color="#fc6603", button_fg_color="#fc6603")
        posicionar(quantas_entradas, 80, 170)
        quantas_entradas.geometry("400x150")
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError or TypeError:
            new_window = custom.CTkToplevel()
            posicionar(new_window)
            new_window.title("Erro")
            new_window.geometry("395x100")
            new_window.wait_visibility()
            new_window.grab_set()

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Arial Bold", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            texto = ("\nValor inválido.")
            console.insert("end", texto)
            console.see("end")
            raise Exception("Valor invalido")

        texto = ("\n##### INICIANDO #####" +
                 "\n" + "Número de entradas: {}".format(numero_entradas)).ljust(50)
        console.insert("end", texto)
        console.see("end")

        # time.sleep(3)
        while i < numero_entradas:
            if kb.is_pressed('end'):
                i = 10000

            texto = ("\nDG número: {}").format(i + 1)
            console.insert("end", texto)
            console.see("end")

            # Dxd_fogo.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                texto = "\nRestam {} entradas".format(restante)
                console.insert("end", texto)
                console.see("end")
            else:
                texto = "\nTODAS AS ENTRADAS FINALIZADAS\n###########"
                console.insert("end", texto)
                console.see("end")

                entradas_finalizadas = custom.CTkToplevel()
                posicionar(entradas_finalizadas)
                entradas_finalizadas.title("Sucesso")
                entradas_finalizadas.geometry("375x100")
                entradas_finalizadas.wait_visibility()
                entradas_finalizadas.grab_set()

                text = custom.CTkLabel(entradas_finalizadas, text="Todas as entradas foram finalizadas.",
                                       font=("Arial Bold", 15))
                text.place(x=60, y=20)
                continuar = custom.CTkButton(entradas_finalizadas, font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", text="Continuar", command=lambda: entradas_finalizadas.destroy())
                continuar.place(x=120, y=60)
                janela.focus_force()
            i += 1
############################################################################################
    if dg == "Arena 5":
        quantas_entradas = custom.CTkInputDialog(text="Quantas entradas?", title=dg,
                                                 font=("Arial Bold", 15), button_hover_color="#fc6603", button_fg_color="#fc6603")
        posicionar(quantas_entradas, 80, 170)
        quantas_entradas.geometry("400x150")
        numero_entradas = quantas_entradas.get_input()
        try:
            numero_entradas = int(numero_entradas)
        except ValueError or TypeError:
            new_window = custom.CTkToplevel()
            posicionar(new_window)
            new_window.title("Erro")
            new_window.geometry("395x100")
            new_window.wait_visibility()
            new_window.grab_set()
            new_window.wait_visibility()
            new_window.grab_set()

            text = custom.CTkLabel(new_window, text="O valor digitado deve ser um número inteiro.", font=("Arial Bold", 15))
            text.place(x=40, y=20)
            ok = custom.CTkButton(new_window, text="Ok", font=("Arial bold", 13), fg_color="#fc6603", hover_color="#fc6603", command=lambda: new_window.destroy())
            ok.place(x=120, y=60)
            texto = ("\nValor inválido.")
            console.insert("end", texto)
            console.see("end")
            raise Exception("Valor invalido")

        texto = ("\n##### INICIANDO #####" +
                 "\n" + "Número de entradas: {}".format(numero_entradas)).ljust(50)
        console.insert("end", texto)
        console.see("end")

        time.sleep(3)
        while i < numero_entradas:
            if kb.is_pressed('end'):
                i = 10000

            texto = ("\nDG número: {}").format(i + 1)
            console.insert("end", texto)
            console.see("end")

            arena_5.play()
            restante = numero_entradas - i - 1
            if restante > 0:
                texto = "\nRestam {} entradas".format(restante)
                console.insert("end", texto)
                console.see("end")
            else:
                texto = "\nTODAS AS ENTRADAS FINALIZADAS\n###########"
                console.insert("end", texto)
                console.see("end")

                entradas_finalizadas = custom.CTkToplevel()
                posicionar(entradas_finalizadas)
                entradas_finalizadas.title("Sucesso")
                entradas_finalizadas.geometry("375x100")
                entradas_finalizadas.wait_visibility()
                entradas_finalizadas.grab_set()

                text = custom.CTkLabel(entradas_finalizadas, text="Todas as entradas foram finalizadas.",
                                       font=("Arial Bold", 15))
                text.place(x=60, y=20)
                continuar = custom.CTkButton(entradas_finalizadas, font=("Arial bold", 13), fg_color="#fc6603",
                                             hover_color="#fc6603", text="Continuar",
                                             command=lambda: entradas_finalizadas.destroy())
                continuar.place(x=120, y=60)

                janela.focus_force()
            i += 1
############################################################################################

def escolher_dg(dg):
    if dg == "Arena 7":
        iniciar("Arena 7")
        # print("1")
    if dg == "Dx desperta gelo":
        iniciar("Dx desperta gelo")
        # print("2")
    if dg == "Dx desperta trem":
        iniciar("Dx desperta trem")
    if dg == "Arena 6":
        iniciar("Arena 6")
    if dg == "Dx desperta fogo":
        iniciar("Dx desperta fogo")
    if dg == "Arena 5":
        iniciar("Arena 5")


# Janela inicial
custom.set_appearance_mode("dark")
janela = custom.CTk()
posicionar(janela, 2, 80)
janela.geometry("800x430")
janela.title("Macro Cabal Online")
janela.resizable(False, False)

img = Image.open("img/login.png")
side_img = custom.CTkImage(dark_image=img, light_image=img, size=(350, 430))
label_img = custom.CTkLabel(janela, image=side_img, text="")
label_img.place(x=0, y=0)

texto = custom.CTkLabel(janela, text="Escolha sua dg", font=("Arial Bold", 24))
texto.place(x=460, y=20)
# Escolher dg
botao_dg = custom.CTkOptionMenu(janela, width=150, height=25, fg_color="#fc6603",
                              font=("Arial Bold", 13), text_color="#ffffff", button_color="#fc6603", button_hover_color="#fc6603",
                              values=["Arena 7", "Arena 6", "Arena 5", "Dx desperta gelo", "Dx desperta trem", "Dx desperta fogo"],
                              command=lambda _: escolher_dg(botao_dg.get()))
botao_dg.place(x=370, y=100)

console = custom.CTkTextbox(janela, activate_scrollbars=True, width=300, height=200)
console.place(x=490, y=230)


janela.mainloop()