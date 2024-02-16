import pydirectinput as pdi
import pyautogui as py
from pyautogui import ImageNotFoundException
import time
import sys, os

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
def clickE(x, y):
    py.moveTo(x, y, duration=0.1)
    py.click(x, y, button="left")
    time.sleep(1)

def clickD(x, y):
    py.moveTo(x, y, duration=0.1)
    py.click(x, y, button="right")
    time.sleep(1)

#DU
def dano():
    pdi.press('1')
    pdi.press('2')
    pdi.press('3')
    pdi.press('4')
    pdi.press('space')

def defesa():
    pdi.press('-')
def potar():
    # clickD(749, 962)
    hotkey('alt','1')
def auto_pot():
    try:
        imagem = "img/auto_pot.png"
        dados = py.locateOnScreen(image=str(resource_path(imagem)), minSearchTime=2, confidence=0.9, grayscale=False)
        dados_ponto = py.center(dados)
        x, y = dados_ponto
        # clickD(749, 962)
        hotkey('alt','1')
        print("Vida abaixou.")
    except ImageNotFoundException:
        pass
def over():
    pdi.press('5')
    time.sleep(1)
    pdi.press('6')
    pdi.press('7')
    pdi.press('8')
def esquiva():
    pdi.press('9')
    time.sleep(1)

def desliza():
    pdi.press('0')
    time.sleep(1)

def ligar_bm2():
    # clickD(1129, 961)
    hotkey('alt', '-')
    time.sleep(1)
    hotkey('alt', '-')
    time.sleep(1)
    hotkey('alt', '-')
    time.sleep(4)

def ligar_bm3():
    hotkey('alt', '2')
    time.sleep(1)
    hotkey('alt', '2')
    time.sleep(1)
    hotkey('alt', '2')
def bm3_atack():
    hotkey('alt', '4')

def bm2_atack():
    # clickD(1168, 968)
    hotkey('alt', '=')
def aproximar():
    # clickD(1096, 964)
    hotkey('alt', '0')
def my_char():
    pdi.press('home')