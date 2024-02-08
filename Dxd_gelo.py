import time
from time import sleep
import pyautogui as py
import pydirectinput as pdi
import skills as sk


def killBoss():
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img\\hpBoss.png', 0.9)
            sk.dano()
        except:
            print(f"Mob morto.")
            hp = 0
def killGate():
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img\\hpPortao.png', 0.9)
            sk.dano()
        except:
            print(f"Portao morto.")
            hp = 0
def localiza(imagem, x):
    dados = py.locateOnScreen(image=imagem, minSearchTime=5, confidence=x, grayscale=True)
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
def play(n):
    i = 0
    while i < n:
        print("entrando dxd gelo")
# #############################################
# ########## Escolhe a dg ##########
        clickE(955, 556)
        # clickE(690, 270)
        # clickE(686, 306)
        # clickE(1082, 677)
        # sleep(2)
        # clickE(852, 704) # Inicia a dg
#
# # #############################################
# #         Primeiro boss automatico
#         clickE(295, 176)
        pdi.press('z')
        killBoss()
# ###############################################
#         try:
#             x, y = localiza('img\\1pilar.png', 0.8)
#             print("Encontrou 1 Pilar")
#             clickE(x, y)
#             sleep(1)
#             missao()
#         except:
#             print("Pilar não encontrado.")
#             quit()
# # #####################################
# #         Caminha para o portão
#         clickE(215, 348)
#         sleep(4)
#         clickE(89, 600)
#         sleep(4)
#         clickE(236, 198)
#         sleep(4)
# ##############################################
#         matar('img\\portao.png', 0.8)
#         clickE(1791, 390)
#         sk.dano()
#         sleep(2)
#
#         try:
#             x, y = localiza('img\\2boss.png', 0.8)
#             print("Nasceu o 2 boss")
#             clickE(x, y)
#         except:
#             print("Mobs pré 2 boss.")
#             pdi.press('z')
#             sk.dano()
#
#         boss('img\\2boss.png', 0.9)
#         pdi.press('space')
#         matar('1bau.png', 0.9)
#         pdi.press('space')
#         pdi.press('space')
#         ##############################################
#         try:
#             x, y = localiza('img\\2pilar.png', 0.8)
#             print("Encontrou 2 Pilar")
#             clickE(x, y)
#             missao()
#         except:
#             print("Pilar não encontrado.")
#         # #####################################
#         clickE(439, 844)
#         sleep(2)
#         clickE(439, 844)
#         sleep(2)
#         clickE(448, 934)
#         sleep(2)
#         clickE(587, 826)
#         sleep(2)
#         clickE(41, 717)
#         sleep(2)
#         clickE(1319, 968)
#         sleep(2)
#         clickE(453, 932)
#         sleep(2)
#         clickE(438, 770)
#         sleep(2)
#         pdi.press('z')
#         hp = 1
#         while hp == 1:
#             try:
#                 x, y = localiza('img\\hpBoss.png', 0.9)
#                 sk.dano()
#             except:
#                 print(f"Ultimo boss morto.")
#                 hp = 0
#         pdi.press('space')
#         pdi.press('space')
#         matar('img\\2bau.png', 0.9)



        i += 1



clickE(955, 556) # click personagem
# clickE(690, 270)
# clickE(686, 306)
# clickE(1082, 677)
# sleep(2)
# clickE(852, 704) # Inicia a dg
#
#
# clickE(295, 176)
# pdi.press('z')
# killBoss()
# try:
#     x, y = localiza('img\\1pilar.png', 0.8)
#     print("Encontrou 1 Pilar")
#     clickE(x, y)
#     sleep(1)
#     missao()
# except:
#     print("Pilar não encontrado.")
#     quit()
#
# py.moveTo(1007, 381)
# sk.esquiva()
# py.moveTo(152, 436)
# sk.esquiva()
# py.moveTo(361,569)
# sk.desliza()
# py.moveTo(269, 938)
# sk.desliza()
# py.moveTo(88, 421)
# sk.desliza()
# py.moveTo(319, 632)
# sk.desliza()
# py.moveTo(839, 282)
# sk.desliza()
#
#
# clickE(1455, 386)
# killGate()
#
# py.moveTo(1399, 554)
# sk.esquiva()
# py.moveTo(1598, 613)
# sk.desliza()
# py.moveTo(1543, 408)
# sk.desliza()
# py.moveTo(1318, 561)
# sk.esquiva()
#
#
# mobsVivos = True
# while mobsVivos:
#     try:
#         x, y = localiza('img\\hpBoss.png', 0.9)
#         killBoss()
#         mobsVivos = False
#     except:
#         print("Mobs vivos ainda!")
#         pdi.press('z')
#         sk.dano()
#
# pdi.press('z')
# sk.dano()
# pdi.press('space')
# pdi.press('space')
# sleep(3)
#
# try:
#     x,y = localiza('img\\2pilar.png', 0.9)
#     print("Encontrou 1 Pilar")
#     clickE(x, y)
#     sleep(2)
# except:
#     try:
#         x, y = localiza('img\\2_0pilar.png', 0.9)
#         print("Encontrou 2 Pilar")
#         clickE(x, y)
#         sleep(2)
#     except:
#         try:
#             x, y = localiza('img\\2_1pilar.png', 0.9)
#             print("Encontrou 2 Pilar")
#             clickE(x, y)
#             sleep(2)
#         except:
#             try:
#                 x, y = localiza('img\\2_2pilar.png', 0.9)
#                 print("Encontrou 2 Pilar")
#                 clickE(x, y)
#                 sleep(2)
#             except:
#                 try:
#                     x, y = localiza('img\\2_3pilar.png', 0.9)
#                     print("Encontrou 2 Pilar")
#                     clickE(x, y)
#                     sleep(2)
#                 except:
#                     try:
#                         x, y = localiza('img\\2_4pilar.png', 0.9)
#                         print("Encontrou 2 Pilar")
#                         clickE(x, y)
#                         sleep(2)
#                     except:
#                         quit()
#
# missao()
#
# x,y = localiza('img\\mancha.png', 0.9)
# py.moveTo(x,y+50)
# sk.esquiva()
#
# py.moveTo(553, 957)
# sk.esquiva()
# py.moveTo(674, 949)
# sk.esquiva()
# py.moveTo(177, 836)
# sk.desliza()
# py.moveTo(190, 742)
# sk.desliza()
# py.moveTo(1128, 1006)
# sk.desliza()
# py.moveTo(1128, 1006)
# sk.esquiva()
# py.moveTo(437, 903)
# sk.desliza()
# py.moveTo(207, 677)
# sk.desliza()
# py.moveTo(262, 969)
# sk.desliza()
#
# pdi.press('z')
# pdi.press('3')
# sleep(5)
# killBoss()
# pdi.press('z')
# pdi.press('3')
# sleep(4)
# pdi.press('space')
# pdi.press('space')
# sleep(1)
# pdi.press('space')
py.moveTo(667, 979)
sk.esquiva()