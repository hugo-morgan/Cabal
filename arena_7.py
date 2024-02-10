from time import sleep
import time
import pyautogui as py
from pyautogui import ImageNotFoundException
import pydirectinput as pdi
import skills as sk
import keyboard as kb


def killBoss():
    # if bm == 'bm2':
    #     sk.ligar_bm2()
    #     start = time.time()
    #     hp = 1
    #     while hp == 1:
    #         end = time.time()
    #
    #         try:
    #             x, y = localiza('img\\hpBoss.png', 0.9)
    #             sk.bm2_atack()
    #             sk.defesa()
    #             sk.potar()
    #         except ImageNotFoundException:
    #             print(f"Mob morto.")
    #             hp = 0
    # else:
    #     hp = 1
    #     while hp == 1:
    #         try:
    #             x, y = localiza('img\\hpBoss.png', 0.9)
    #             sk.dano()
    #             sk.defesa()
    #             sk.potar()
    #         except ImageNotFoundException:
    #             print(f"Mob morto.")
    #             hp = 0
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img\\hpBoss.png', 0.9)
            sk.dano()
            sk.defesa()
            sk.potar()
        except ImageNotFoundException:
            print(f"Mob morto.")
            hp = 0

def killGate():
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img\\arena_7\\hpPortao.png', 0.9)
            sk.dano()
        except ImageNotFoundException:
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


def captar_mouse():
    script = []
    quit = False
    while quit == False:
        if kb.is_pressed('9'):
            x, y = py.position()
            mousepos = [x, y, 'sk.esquiva()']
            script.append(mousepos)
            print(script)
            sleep(1)

        if kb.is_pressed('0'):
            x, y = py.position()
            mousepos = [x, y, 'sk.desliza()']
            script.append(mousepos)
            print(script)
            sleep(1)

        if kb.is_pressed('shift'):
            quit = True
            sleep(1)
    return script


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
    print("entrando arena 7")
    clickE(955, 556)  # click personagem

    clickE(730, 270)
    sleep(3)
    clickE(737, 328)
    clickE(1082, 679)
    sleep(2)
    clickE(850, 703)  # inicia dg

    anda_portao = [[1347, 283, 'sk.esquiva()'], [1051, 174, 'sk.desliza()'], [1566, 279, 'sk.esquiva()'], [1437, 204, 'sk.desliza()'], [1683, 344, 'sk.esquiva()'], [1263, 293, 'sk.desliza()'], [175, 295, 'sk.esquiva()'], [175, 295, 'sk.desliza()'], [175, 295, 'sk.esquiva()'], [175, 295, 'sk.desliza()'], [315, 282, 'sk.esquiva()']]
    executar_script(anda_portao)

    pdi.press('z')
    killGate()

    centraliza = [[363, 276, 'sk.desliza()'], [150, 748, 'sk.esquiva()'], [258, 237, 'sk.desliza()'], [358, 354, 'sk.desliza()']]
    executar_script(centraliza)

    mobsVivos = True
    while mobsVivos:
        try:
            x, y = localiza('img\\hpBoss.png', 0.9)
            sk.over()
            killBoss()
            mobsVivos = False
        except ImageNotFoundException:
            print("Mobs vivos ainda!")
            pdi.press('z')
            sk.dano()

    bau = True
    while bau:
        try:
            x, y = localiza('img\\arena_7\\bau_legendario.png', 0.9)
            print("Baú encontrado.")
            bau = False
        except ImageNotFoundException:
            print("Baú não encontrado ainda!")
            pdi.press('z')

    sk.dano()

    pdi.press('space', presses=10, interval=1)
    clickE(983, 497)  # clica em ok
    clickE(734, 554)  # tesouro dez guilda
    clickE(370, 552)  # dado
    clickE(321, 554)  # sai da dg
    sleep(2)
    print("dg finalizada")
play()