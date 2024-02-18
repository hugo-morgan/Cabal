from time import sleep
import time
import pyautogui as py
from pyautogui import ImageNotFoundException
import pydirectinput as pdi
import skills as sk
import sys
import os
import keyboard as kb


def hotkey(tecla1, tecla2):
    pdi.keyDown(tecla1)
    pdi.keyDown(tecla2)
    pdi.keyUp(tecla2)
    pdi.keyUp(tecla1)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


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
                    x, y = localiza('img/hpBoss.png', 0.9)
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
                    x, y = localiza('img/hpBoss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0

            else:
                try:
                    x, y = localiza('img/hpBoss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0
    elif bm == 'bm3':
        sk.ligar_bm3()
        start = time.time()
        hp = 1
        bm3 = True
        print("BM3 ativa")
        while hp == 1:
            end = time.time()
            tempo_bm = end - start

            if tempo_bm <= 80.00:
                try:
                    x, y = localiza('img/hpBoss.png', 0.9)
                    sk.bm3_atack()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    clickD(192, 116)  # Desliga BM
                    bm3 = False
                    hp = 0

            elif tempo_bm > 80.00 and bm3 == True:
                clickD(192, 116)  # Desliga BM
                bm3 = False
                print("BM3 finalizada")
                try:
                    x, y = localiza('img/hpBoss.png', 0.9)
                    sk.dano()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0

                else:
                    try:
                        x, y = localiza('img/hpBoss.png', 0.9)
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
                x, y = localiza('img/hpBoss.png', 0.9)
                sk.dano()
            except ImageNotFoundException:
                print(f"Mob morto.")
                hp = 0


def killGate():
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img/hpPortao.png', 0.9)
            sk.dano()
        except ImageNotFoundException:
            print(f"Portao morto.")
            hp = 0


def localiza(imagem, x):
    dados = py.locateOnScreen(image=imagem, minSearchTime=5, confidence=x, grayscale=True)
    dados_ponto = py.center(dados)
    x, y = dados_ponto
    if kb.is_pressed('end'):
        sleep(0.5)
        py.moveTo(0, 0)
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
    print("entrando dxd gelo")
    ###########################################
    clickE(955, 556)  # click personagem
    clickE(690, 270)
    clickE(686, 306)
    clickE(1082, 677)
    sleep(2)
    clickE(852, 704)  # Inicia a dg

    clickE(295, 176)
    pdi.press('z')
    sk.aproximar()
    killBoss()

    py.moveTo(960, 0)
    try:
        x, y = localiza('img/dxd_gelo/ref1.png', 0.85)
        clickE(x, y)
        sleep(1)
    except ImageNotFoundException:
        try:
            x, y = localiza('img/dxd_gelo/ref1_1.png', 0.85)
            clickE(x, y)
            sleep(1)
        except ImageNotFoundException:
            quit()
    py.moveTo(960, 0)
    try:
        x, y = localiza('img/dxd_gelo/1pilar.png', 0.8)
        print("Encontrou 1 Pilar")
        clickE(x, y)
        sleep(1)
    except ImageNotFoundException:
        try:
            x, y = localiza('img/dxd_gelo/1_0pilar.png', 0.9)
            print("Encontrou 1 Pilar")
            clickE(x, y)
            sleep(1)
        except ImageNotFoundException:
            print("Pilar não encontrado.")
            quit()
    missao()

    py.moveTo(1007, 381)
    sk.esquiva()
    py.moveTo(152, 436)
    sk.esquiva()
    py.moveTo(361, 569)
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
            x, y = localiza('img/hpBoss.png', 0.9, minsearch=2)
            killBoss('bm2')
            clickD(192, 116)  # Desliga BM
            sleep(1)
            mobsVivos = False
        except ImageNotFoundException:
            print("Mobs vivos ainda!")
            pdi.press('z')
            sk.dano()

    pdi.press('z')
    sk.dano()
    pdi.press('space')
    pdi.press('space')
    sleep(3)

    py.moveTo(1383, 624)
    sk.esquiva()

    py.moveTo(960, 0)
    try:
        x, y = localiza('img/dxd_gelo/mancha.png', 0.85)
        py.moveTo(x, y + 50)
        sk.esquiva()
    except ImageNotFoundException:
        try:
            x, y = localiza('img/dxd_gelo/mancha1.png', 0.85)
            py.moveTo(x, y + 40)
            sk.esquiva()
        except ImageNotFoundException:
            quit()

    py.moveTo(960, 0)
    try:
        x, y = localiza('img/dxd_gelo/2pilar.png', 0.8)
        print("Encontrou 2 Pilar")
        clickE(x, y)
        sleep(2)
    except ImageNotFoundException:
        try:
            x, y = localiza('img/dxd_gelo/2_0pilar.png', 0.8)
            print("Encontrou 2 Pilar")
            clickE(x, y)
            sleep(2)
        except ImageNotFoundException:
            try:
                x, y = localiza('img/dxd_gelo/2_1pilar.png', 0.8)
                print("Encontrou 2 Pilar")
                clickE(x, y)
                sleep(2)
            except ImageNotFoundException:
                try:
                    x, y = localiza('img/dxd_gelo/2_2pilar.png', 0.8)
                    print("Encontrou 2 Pilar")
                    clickE(x, y)
                    sleep(2)
                except ImageNotFoundException:
                    try:
                        x, y = localiza('img/dxd_gelo/2_3pilar.png', 0.8)
                        print("Encontrou 2 Pilar")
                        clickE(x, y)
                        sleep(2)
                    except ImageNotFoundException:
                        try:
                            x, y = localiza('img/dxd_gelo/2_4pilar.png', 0.8)
                            print("Encontrou 2 Pilar")
                            clickE(x, y)
                            sleep(2)
                        except ImageNotFoundException:
                            try:
                                x, y = localiza('img/dxd_gelo/2_5pilar.png', 0.8)
                                print("Encontrou 2 Pilar")
                                clickE(x, y)
                                sleep(2)
                            except ImageNotFoundException:
                                quit()

    missao()

    py.moveTo(960, 0)
    try:
        x, y = localiza('img/dxd_gelo/mancha.png', 0.9)
        py.moveTo(x, y + 50)
        sk.esquiva()
    except ImageNotFoundException:
        pass

    script = [[634, 967, 'sk.esquiva()'], [619, 970, 'sk.esquiva()'], [619, 763, 'sk.esquiva()'],
              [219, 789, 'sk.desliza()'], [700, 881, 'sk.esquiva()'], [638, 973, 'sk.desliza()'],
              [638, 973, 'sk.esquiva()'], [329, 695, 'sk.desliza()'], [808, 865, 'sk.esquiva()'],
              [395, 685, 'sk.desliza()'], [578, 831, 'sk.esquiva()']]

    executar_script(script)

    pdi.press('z')
    pdi.press('3')
    sleep(3)
    sk.over()
    killBoss()

    # bau
    sleep(2)
    pdi.press('z')
    pdi.press('3')
    sleep(4)
    pdi.press('space', presses=6, interval=1)

    py.moveTo(667, 979)
    sk.esquiva()
    py.moveTo(1012, 886)
    sk.esquiva()
    py.moveTo(960, 0)
    try:
        x, y = localiza('img/dxd_gelo/3_0pilar.png', 0.9)
        print("Encontrou 1 Pilar")
        clickE(x, y)
        sleep(2)
    except ImageNotFoundException:
        try:
            x, y = localiza('img/dxd_gelo/3_1pilar.png', 0.9)
            print("Encontrou 2 Pilar")
            clickE(x, y)
            sleep(2)
        except ImageNotFoundException:
            try:
                x, y = localiza('img/dxd_gelo/3_2pilar.png', 0.9)
                print("Encontrou 2 Pilar")
                clickE(x, y)
                sleep(2)
            except ImageNotFoundException:
                try:
                    x, y = localiza('img/dxd_gelo/3_3pilar.png', 0.9)
                    print("Encontrou 2 Pilar")
                    clickE(x, y)
                    sleep(2)
                except ImageNotFoundException:
                    try:
                        x, y = localiza('img/dxd_gelo/3_4pilar.png', 0.9)
                        print("Encontrou 2 Pilar")
                        clickE(x, y)
                        sleep(2)
                    except ImageNotFoundException:
                        quit()
    missao()

    # Finalização da dg
    clickE(983, 497)
    clickE(734, 554)  # tesouro de guilda
    clickE(370, 552)  # dado
    clickE(321, 554)  # sai da dg
    clickD(192, 116)  # Desliga BM
    sleep(2)
    print("dg finalizada")
