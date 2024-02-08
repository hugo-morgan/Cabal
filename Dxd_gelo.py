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
# ##    ###########################################
        clickE(955, 556) # click personagem
        clickE(690, 270)
        clickE(686, 306)
        clickE(1082, 677)
        sleep(2)
        clickE(852, 704) # Inicia a dg

        clickE(295, 176)
        pdi.press('z')
        killBoss()

        py.moveTo(960, 0)
        try:
            x, y = localiza('img\\ref1.png', 0.9)
            clickE(x, y)
            sleep(1)
        except:
            try:
                x, y = localiza('img\\ref1_1.png', 0.9)
                clickE(x, y)
                sleep(1)
            except:
                quit()
        py.moveTo(960, 0)
        try:
            x, y = localiza('img\\1pilar.png', 0.8)
            print("Encontrou 1 Pilar")
            clickE(x, y)
            sleep(1)
        except:
            try:
                x, y = localiza('img\\1_0pilar.png', 0.9)
                print("Encontrou 1 Pilar")
                clickE(x, y)
                sleep(1)
            except:
                print("Pilar não encontrado.")
                quit()
        missao()

        py.moveTo(1007, 381)
        sk.esquiva()
        py.moveTo(152, 436)
        sk.esquiva()
        py.moveTo(361,569)
        sk.desliza()
        py.moveTo(269, 938)
        sk.desliza()
        py.moveTo(88, 421)
        sk.desliza()
        py.moveTo(319, 632)
        sk.desliza()
        py.moveTo(839, 282)
        sk.desliza()


        clickE(1455, 386)
        killGate()

        py.moveTo(1399, 554)
        sk.esquiva()
        py.moveTo(1598, 613)
        sk.desliza()
        py.moveTo(1543, 408)
        sk.desliza()
        py.moveTo(1318, 561)
        sk.esquiva()


        mobsVivos = True
        while mobsVivos:
            try:
                x, y = localiza('img\\hpBoss.png', 0.9)
                killBoss()
                mobsVivos = False
            except:
                print("Mobs vivos ainda!")
                pdi.press('z')
                sk.dano()

        pdi.press('z')
        sk.dano()
        pdi.press('space')
        pdi.press('space')
        sleep(3)

        py.moveTo(960, 0)
        try:
            x,y = localiza('img\\mancha.png', 0.9)
            py.moveTo(x,y+50)
            sk.esquiva()
        except:
            pass

        py.moveTo(960, 0)
        try:
            x,y = localiza('img\\2pilar.png', 0.8)
            print("Encontrou 2 Pilar")
            clickE(x, y)
            sleep(2)
        except:
            try:
                x, y = localiza('img\\2_0pilar.png', 0.8)
                print("Encontrou 2 Pilar")
                clickE(x, y)
                sleep(2)
            except:
                try:
                    x, y = localiza('img\\2_1pilar.png', 0.8)
                    print("Encontrou 2 Pilar")
                    clickE(x, y)
                    sleep(2)
                except:
                    try:
                        x, y = localiza('img\\2_2pilar.png', 0.8)
                        print("Encontrou 2 Pilar")
                        clickE(x, y)
                        sleep(2)
                    except:
                        try:
                            x, y = localiza('img\\2_3pilar.png', 0.8)
                            print("Encontrou 2 Pilar")
                            clickE(x, y)
                            sleep(2)
                        except:
                            try:
                                x, y = localiza('img\\2_4pilar.png', 0.8)
                                print("Encontrou 2 Pilar")
                                clickE(x, y)
                                sleep(2)
                            except:
                                try:
                                    x, y = localiza('img\\2_5pilar.png', 0.8)
                                    print("Encontrou 2 Pilar")
                                    clickE(x, y)
                                    sleep(2)
                                except:
                                    quit()

        missao()

        py.moveTo(960, 0)
        try:
            x,y = localiza('img\\mancha.png', 0.9)
            py.moveTo(x,y+50)
            sk.esquiva()
        except:
            pass

        py.moveTo(553, 957)
        sk.esquiva()
        py.moveTo(674, 949)
        sk.esquiva()
        py.moveTo(177, 836)
        sk.desliza()
        py.moveTo(190, 742)
        sk.desliza()
        py.moveTo(1128, 1006)
        sk.desliza()
        py.moveTo(1128, 1006)
        sk.esquiva()
        py.moveTo(437, 903)
        sk.desliza()
        py.moveTo(207, 677)
        sk.desliza()
        py.moveTo(262, 969)
        sk.desliza()

        pdi.press('z')
        pdi.press('3')
        sleep(5)
        killBoss()
        pdi.press('z')
        pdi.press('3')
        sleep(4)
        pdi.press('space')
        pdi.press('space')
        sleep(1)
        pdi.press('space')


        py.moveTo(667, 979)
        sk.esquiva()
        py.moveTo(1012, 886)
        sk.esquiva()
        py.moveTo(960, 0)
        try:
            x,y = localiza('img\\3_0pilar.png', 0.9)
            print("Encontrou 1 Pilar")
            clickE(x, y)
            sleep(2)
        except:
            try:
                x, y = localiza('img\\3_1pilar.png', 0.9)
                print("Encontrou 2 Pilar")
                clickE(x, y)
                sleep(2)
            except:
                try:
                    x, y = localiza('img\\3_2pilar.png', 0.9)
                    print("Encontrou 2 Pilar")
                    clickE(x, y)
                    sleep(2)
                except:
                    try:
                        x, y = localiza('img\\3_3pilar.png', 0.9)
                        print("Encontrou 2 Pilar")
                        clickE(x, y)
                        sleep(2)
                    except:
                        try:
                            x, y = localiza('img\\3_4pilar.png', 0.9)
                            print("Encontrou 2 Pilar")
                            clickE(x, y)
                            sleep(2)
                        except:
                            quit()
        missao()

        # Finalização da dg
        clickE(983, 497)
        clickE(734, 554) # tesouro de guilda
        clickE(370, 552) # dado
        clickE(321, 554) # sai da dg
        sleep(2)

        print(f"Entrada número: {i+1}")
        i += 1