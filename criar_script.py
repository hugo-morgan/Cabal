import time
from time import sleep
import pyautogui as py
from pyautogui import ImageNotFoundException
import pydirectinput as pdi
import skills as sk
import keyboard as kb


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

import mouse
def captar_mouse():
    script = []
    quit = False
    while quit == False:
        if kb.is_pressed('9'):
            x, y = py.position()
            mousepos = [x, y, 'sk.esquiva()']
            script.append(mousepos)
            sleep(1)

        if kb.is_pressed('0'):
            x, y = py.position()
            mousepos = [x, y, 'sk.desliza()']
            script.append(mousepos)
            sleep(1)
# Colocar aqui o if do click do mouse
        if kb.is_pressed('.'):
            x, y = py.position()
            mousepos = [x, y, 'drag']
            script.append(mousepos)
            sleep(0.3)
        if kb.is_pressed('ctrl'):
            x, y = py.position()
            mousepos = [x, y, 'first_drag']
            script.append(mousepos)
            sleep(0.3)



        if kb.is_pressed('shift'):
            quit = True
            sleep(1)
    print(script)
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
        if _[2] == 'first_drag':
            py.moveTo(x, y)

        if _[2] == 'drag':
            py.dragTo(x, y, button='left', duration=0.4)




clickE(955, 556)

quit = False
script = []
while quit == False:

    py.dragTo()


    if kb.is_pressed('shift'):
        quit = True
        sleep(1)
