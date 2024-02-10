import pydirectinput as pdi
import pyautogui as py
import time

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
    clickD(749, 962)
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
    clickD(1129, 961)
    time.sleep(1)
    clickD(1129, 961)
    time.sleep(1)
    clickD(1129, 961)
    time.sleep(4)

def bm2_atack():
    clickD(1168, 968)

def aproximar():
    clickD(1096, 964)