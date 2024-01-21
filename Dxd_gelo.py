from time import sleep
import pyautogui as py
import pydirectinput as pdi
import skills as sk

def matar(mob, x):
    f = 0
    while f == 0:
        try:
            x, y = localiza(mob, x)
            f = 1
            print(f"{mob} encontrado.")
            clickE(x, y)
            hp = 1
            while hp == 1:
                try:
                    x, y = localiza('img\\hpBoss.png', 0.9)
                    sk.dano()
                except:
                    print(f"{mob} morto.")
                    hp = 0
        except:
            f = 0
            print(f"{mob} não encontrado.")
def boss(mob, x):
    f = 0
    while f == 0:
        try:
            x, y = localiza(mob, x)
            f = 1
            print(f"Começa a matar o {mob}")
            clickE(x, y)
            sk.over()
            hp = 1
            while hp == 1:
                try:
                    x, y = localiza('img\\hpBoss.png', 0.9)
                    sk.dano()
                except:
                    print(f"{mob} morto.")
                    hp = 0
        except:
            f = 0
def localiza(imagem, x):
    dados = py.locateOnScreen(image=imagem, confidence=x)
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
        clickE(690, 270)
        clickE(686, 306)
        clickE(1082, 677)
        sleep(2)
        clickE(852, 704) # Inicia a dg

# #############################################
#         Primeiro boss automatico
        clickE(295, 176)
        matar('img\\1boss.png', 0.9)
# ###############################################
        f = 0
        while f == 0:
            try:
                x, y = localiza('img\\1pilar.png', 0.8)
                f = 1
                print("Encontrou 1 Pilar")
                clickE(x, y)
                sleep(1)
                missao()
            except:
                f = 0
                print("Pilar não encontrado.")
# #####################################
#         Caminha para o portão
        clickE(215, 348)
        sleep(4)
        clickE(89, 600)
        sleep(4)
        clickE(236, 198)
        sleep(4)
##############################################
        matar('img\\portao.png', 0.8)
        clickE(1791, 390)
        sk.dano()
        sleep(2)
        f = 0
        while f == 0:
            try:
                x, y = localiza('img\\2boss.png', 0.8)
                f = 1
                print("Nasceu o 2 boss")
                clickE(x, y)
            except:
                f = 0
                print("Mobs pré 2 boss.")
                pdi.press('z')
                sk.dano()

        boss('img\\2boss.png', 0.9)
        pdi.press('space')
        matar('1bau.png', 0.9)
        pdi.press('space')
        pdi.press('space')
        ##############################################
        f = 0
        while f == 0:
            try:
                x, y = localiza('img\\2pilar.png', 0.8)
                f = 1
                print("Encontrou 2 Pilar")
                clickE(x, y)
                missao()
            except:
                f = 0
                print("Pilar não encontrado.")
        # #####################################
        clickE(439, 844)
        sleep(2)
        clickE(439, 844)
        sleep(2)
        clickE(448, 934)
        sleep(2)
        clickE(587, 826)
        sleep(2)
        clickE(41, 717)
        sleep(2)
        clickE(1319, 968)
        sleep(2)
        clickE(453, 932)
        sleep(2)
        clickE(438, 770)
        sleep(2)
        pdi.press('z')
        hp = 1
        while hp == 1:
            try:
                x, y = localiza('img\\hpBoss.png', 0.9)
                sk.dano()
            except:
                print(f"Ultimo boss morto.")
                hp = 0
        pdi.press('space')
        pdi.press('space')
        matar('img\\2bau.png', 0.9)



        i += 1
