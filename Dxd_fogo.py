from time import sleep
import time
import pyautogui as py
from pyautogui import ImageNotFoundException
import pydirectinput as pdi
import skills as sk
import customtkinter as custom
import keyboard as kb

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

def killBoss(bm=""):
    if bm == 'bm2':  # 90s de BM2
        sk.ligar_bm2()
        start = time.time()
        hp = 1
        bm2 = True
        print("BM2 ativa")
        while hp == 1:
            end = time.time()
            tempo_bm = end - start

            if tempo_bm <= 80.00:
                try:
                    x, y = localiza('img\\hpBoss.png', 0.9)
                    sk.bm2_atack()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    clickD(192, 116)  # Desliga BM
                    bm2 = False
                    hp = 0

            elif tempo_bm > 80.00 and bm2 == True:
                clickD(192, 116)  # Desliga BM
                bm2 = False
                print("BM2 finalizada")
                try:
                    x, y = localiza('img\\hpBoss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0

            else:
                try:
                    x, y = localiza('img\\hpBoss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0
    else:
        hp = 1
        while hp == 1:
            try:
                x, y = localiza('img\\hpBoss.png', 0.9)
                sk.dano()
            except ImageNotFoundException:
                print(f"Mob morto.")
                hp = 0

def killBoss2(bm=""):
    if bm == 'bm2':  # 90s de BM2
        sk.ligar_bm2()
        start = time.time()
        hp = 1
        bm2 = True
        print("BM2 ativa")
        while hp == 1:
            end = time.time()
            tempo_bm = end - start

            if tempo_bm <= 80.00:
                try:
                    x, y = localiza('img\\hpBoss2.png', 0.9)
                    sk.bm2_atack()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    clickD(192, 116)  # Desliga BM
                    bm2 = False
                    hp = 0

            elif tempo_bm > 80.00 and bm2 == True:
                clickD(192, 116)  # Desliga BM
                bm2 = False
                print("BM2 finalizada")
                try:
                    x, y = localiza('img\\dxd_trem\\1boss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0

            else:
                try:
                    x, y = localiza('img\\dxd_trem\\1boss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0
    else:
        hp = 1
        while hp == 1:
            try:
                x, y = localiza('img\\dxd_trem\\1boss.png', 0.9)
                sk.dano()
            except ImageNotFoundException:
                print(f"Mob morto.")
                hp = 0

def killGate():
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img\\hpPortao.png', 0.9)
            sk.dano()
        except ImageNotFoundException:
            print(f"Portao morto.")
            hp = 0


def localiza(imagem, x, minsearch=5):
    dados = py.locateOnScreen(image=imagem, minSearchTime=minsearch, confidence=x, grayscale=True)
    dados_ponto = py.center(dados)
    x, y = dados_ponto
    return x, y


def missao():
    i = 0
    while i < 6:
        pdi.press('space')
        i += 1


def clickE(x, y):
    py.moveTo(x, y, duration=0.1)
    py.click(x, y, button="left")
    sleep(1)


def clickD(x, y):
    py.moveTo(x, y, duration=0.1)
    py.click(x, y, button="right")
    time.sleep(1)


def executar_script(script):
    clickE(955, 556)  # click personagem
    for _ in script:
        x = _[0]
        y = _[1]
        if _[2] == 'sk.desliza()':
            py.moveTo(x, y)
            sk.desliza()
        if _[2] == 'sk.esquiva()':
            py.moveTo(x, y)
            sk.esquiva()

def play():

    print("entrando dxd fogo")
    ###########################################

    clickE(955, 556)  # click personagem

    # pdi.press('z')
    # sk.dano()
    # clickE(998, 173)
    # sleep(1)
    # clickE(700, 307)
    # clickE(1066, 681)
    # clickE(848, 703) # Inicia dg
#
# # # 1 Boss
#     script = [[1093, 387, 'sk.desliza()'], [670, 545, 'sk.esquiva()']]
#     executar_script(script)
#
#     sk.over()
#     pdi.press('z')
#     killBoss('bm2')
#
# # # Baú
#     pdi.press('z')
#     sk.dano()
#     pdi.press('space', presses=3, interval=1)
#
#     script = [[1280, 369, 'sk.desliza()'], [1029, 359, 'sk.esquiva()'], [1307, 274, 'sk.desliza()'], [1199, 232, 'sk.esquiva()'], [1336, 235, 'sk.desliza()'], [992, 167, 'sk.esquiva()'], [1334, 183, 'sk.desliza()'], [1334, 183, 'sk.esquiva()'], [1469, 309, 'sk.desliza()'], [1435, 293, 'sk.esquiva()'], [1739, 500, 'sk.desliza()'], [1492, 414, 'sk.esquiva()']]
#     executar_script(script)
#
# # # Boss do portão 1
#     bossNotFound = True
#     while bossNotFound:
#         try:
#             x, y = localiza('img\\hpBoss2.png', 0.9, minsearch=1)
#             killBoss2()
#             bossNotFound = False
#         except ImageNotFoundException:
#             pdi.press('z')
#
#
# # Boss do portão 2
#     script = [[1324, 568, 'sk.esquiva()'], [1451, 438, 'sk.desliza()'], [1290, 744, 'sk.esquiva()'], [1777, 564, 'sk.desliza()'], [1435, 939, 'sk.esquiva()'], [1146, 114, 'sk.desliza()'], [1351, 202, 'sk.esquiva()'], [1155, 197, 'sk.desliza()'], [994, 183, 'sk.esquiva()'], [770, 158, 'sk.desliza()'], [577, 270, 'sk.esquiva()'], [701, 386, 'sk.desliza()'], [1384, 518, 'sk.desliza()'], [1338, 591, 'sk.esquiva()']]
#     executar_script(script)

#     bossNotFound = True
#     while bossNotFound:
#         try:
#             x, y = localiza('img\\hpBoss2.png', 0.9, minsearch=1)
#             killBoss2()
#             bossNotFound = False
#         except ImageNotFoundException:
#             pdi.press('z')
#
#     script = [[316, 753, 'sk.desliza()'], [601, 866, 'sk.esquiva()'], [517, 680, 'sk.desliza()'], [519, 887, 'sk.esquiva()'], [1159, 211, 'sk.desliza()'], [930, 208, 'sk.esquiva()'], [1186, 207, 'sk.desliza()'], [935, 206, 'sk.esquiva()'], [1232, 233, 'sk.desliza()'], [1448, 410, 'sk.esquiva()'], [1247, 319, 'sk.desliza()'], [1588, 718, 'sk.esquiva()'], [828, 261, 'sk.desliza()'], [1371, 480, 'sk.esquiva()']]
#     executar_script(script)
#
#     pdi.press('z')
#     sk.dano()
#
#     script = [[1487, 371, 'sk.desliza()'], [1677, 602, 'sk.esquiva()'], [1773, 613, 'sk.desliza()'], [1689, 694, 'sk.esquiva()'], [1573, 715, 'sk.desliza()']]
#     executar_script(script)
#
# # Ultimo boss
#     pdi.press('z')
#     killBoss('bm2')
# # # Bau
#     sleep(1)
#     pdi.press('z')
#     sk.dano()
#     pdi.press('space', presses=4, interval=1)
#     sleep(2)
#
# # Finalização da dg
#     clickE(983, 497)
#     clickE(734, 554)  # tesouro de guilda
#     clickE(370, 552)  # dado
#     clickE(321, 554)  # sai da dg
#     clickD(192, 116)  # Desliga BM
#     sleep(2)
#     print("dg finalizada")


def att(x, texto):
    x.configure(state="normal")
    x.insert("end", texto)
    x.configure(state="disabled")

# janela = custom.CTk()
# posicionar(janela, 2, 80)
# janela.geometry("270x230")
# janela.title("Console")
# janela.resizable(False, False)
#
# console = custom.CTkTextbox(janela, activate_scrollbars=True, width=260, height=150)
# console.place(x=5, y=5)
# janela.attributes("-topmost", True)
#
# play()
#
#
#
#
#
#
# janela.mainloop()