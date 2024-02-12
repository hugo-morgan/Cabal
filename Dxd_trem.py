from time import sleep
import time
import pyautogui as py
from pyautogui import ImageNotFoundException
import pydirectinput as pdi
import skills as sk
import keyboard as kb


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

def killBoss1(bm=""):
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
                    x, y = localiza('img\\dxd_trem\\1boss.png', 0.9)
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
    print("entrando dxd trem")
    ###########################################
    clickE(955, 556)  # click personagem
    clickE(1296, 447)
    clickE(736, 306)
    clickE(1068, 681)
    clickE(848, 703) # Inicia dg

    script = [[1035, 276, 'sk.esquiva()'], [1014, 338, 'sk.desliza()']]
    executar_script(script)

    clickE(958, 488)
    missao()

    hp = 1
    while hp == 1:
        try:
            pdi.press('z')
            x, y = localiza('img\\hpPortao.png', 0.9)
            sk.dano()
        except ImageNotFoundException:
            print(f"Mobs mortos.")
            hp = 0

    script = [[624, 607, 'sk.esquiva()'], [624, 608, 'sk.desliza()'], [624, 608, 'sk.esquiva()'], [1245, 279, 'sk.desliza()'], [877, 344, 'sk.esquiva()'], [1139, 293, 'sk.desliza()'], [727, 310, 'sk.esquiva()'], [1078, 292, 'sk.desliza()']]
    executar_script(script)

    clickE(917, 344)
    missao()

    script = [[1031, 213, 'sk.desliza()'], [1031, 213, 'sk.esquiva()']]
    executar_script(script)

    clickE(955, 385)
    missao()

    hp = 1
    while hp == 1:
        try:
            pdi.press('z')
            x, y = localiza('img\\hpPortao.png', 0.9)
            sk.dano()
        except ImageNotFoundException:
            print(f"Mobs mortos.")
            hp = 0

    script = [[624, 607, 'sk.esquiva()'], [624, 608, 'sk.desliza()'], [624, 608, 'sk.esquiva()'], [1245, 279, 'sk.desliza()'], [877, 344, 'sk.esquiva()'], [1139, 293, 'sk.desliza()'], [727, 310, 'sk.esquiva()'], [1078, 292, 'sk.desliza()']]
    executar_script(script)

    clickE(917, 344)
    missao()

    script = [[1041, 264, 'sk.desliza()'], [1049, 364, 'sk.esquiva()']]
    executar_script(script)
    clickE(969, 461)
    missao()

    sleep(1)
    pdi.press('z')
    sk.over()
    killBoss1()

    pdi.press('z')
    sk.dano()
    pdi.press('space')
    sleep(1)
    pdi.press('space')
    sleep(1)
    pdi.press('space')

    script = [[624, 607, 'sk.esquiva()'], [624, 608, 'sk.desliza()'], [624, 608, 'sk.esquiva()'], [1245, 279, 'sk.desliza()'], [877, 344, 'sk.esquiva()'], [1139, 293, 'sk.desliza()'], [727, 310, 'sk.esquiva()'], [1078, 292, 'sk.desliza()']]
    executar_script(script)
    clickE(917, 344)
    missao()

    script = [[1041, 264, 'sk.desliza()'], [1049, 364, 'sk.esquiva()']]
    executar_script(script)
    clickE(969, 461)
    missao()

    sleep(5)
    hp = 1
    while hp == 1:
        try:
            sleep(6)
            pdi.press('z')
            x, y = localiza('img\\hpPortao.png', 0.9)
            sk.dano()
        except ImageNotFoundException:
            print(f"Mobs mortos.")
            hp = 0

    script = [[624, 607, 'sk.esquiva()'], [624, 608, 'sk.desliza()'], [624, 608, 'sk.esquiva()'], [1245, 279, 'sk.desliza()'], [877, 344, 'sk.esquiva()'], [1139, 293, 'sk.desliza()'], [727, 310, 'sk.esquiva()'], [1078, 292, 'sk.desliza()']]
    executar_script(script)

    clickE(917, 344)
    missao()

    script = [[1041, 264, 'sk.desliza()'], [1049, 364, 'sk.esquiva()']]
    executar_script(script)
    clickE(969, 461)
    missao()

    script = [[624, 607, 'sk.esquiva()'], [624, 608, 'sk.desliza()'], [624, 608, 'sk.esquiva()'], [1245, 279, 'sk.desliza()'], [877, 344, 'sk.esquiva()'], [1139, 293, 'sk.desliza()'], [727, 310, 'sk.esquiva()'], [1078, 292, 'sk.desliza()']]
    executar_script(script)

    bossNotFound = True
    while bossNotFound:
        try:
            x, y = localiza('img\\hpBoss.png', 0.9, minsearch=1)
            sk.over()
            killBoss()
            bossNotFound = False
        except ImageNotFoundException:
            print("Boss não encontrado")
            pdi.press('z')

    sleep(1)
    pdi.press('z')
    sk.dano()
    pdi.press('space')
    sleep(1)
    pdi.press('space')
    sleep(1)
    pdi.press('space')


    script = [[812, 505, 'sk.desliza()'], [1270, 473, 'sk.esquiva()'], [1258, 745, 'sk.esquiva()']]
    executar_script(script)
    clickE(871, 354)
    missao()
    sleep(2)

    # Finalização da dg
    clickE(983, 497)
    clickE(734, 554)  # tesouro de guilda
    clickE(370, 552)  # dado
    clickE(321, 554)  # sai da dg
    clickD(192, 116)  # Desliga BM
    sleep(2)
    print("dg finalizada")