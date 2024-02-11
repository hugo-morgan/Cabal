from time import sleep
import time
import pyautogui as py
from pyautogui import ImageNotFoundException
import pydirectinput as pdi
import skills as sk
import keyboard as kb

def killBoss(bm=""):
    if bm == 'bm2': # 90s de BM2
        sk.ligar_bm2()
        start = time.time()
        hp = 1
        bm2 = True
        print("BM2 ativa")
        while hp == 1:
            end = time.time()
            tempo_bm = end - start

            if tempo_bm <= 10.00:
                try:
                    x, y = localiza('img\\hpBoss.png', 0.9)
                    sk.bm2_atack()
                    sk.defesa()
                    sk.potar()
                except ImageNotFoundException:
                    print(f"Mob morto.")
                    hp = 0
            elif tempo_bm > 10.00 and bm2 == True:
                clickD(192,116) # Desliga BM
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

def killGate():
    hp = 1
    while hp == 1:
        try:
            x, y = localiza('img\\hpPortao.png', 0.9)
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
    # clickE(955, 556)  # click personagem
    #
    #
    #
    # # Finalização da dg
    # clickE(983, 497)
    # clickE(734, 554)  # tesouro de guilda
    # clickE(370, 552)  # dado
    # clickE(321, 554)  # sai da dg
    # clickD(192, 116)  # Desliga BM
    # sleep(2)
    print("dg finalizada")

