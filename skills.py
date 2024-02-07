import pydirectinput as pdi
import pyautogui as py
import time

def clickE(x, y):
    py.moveTo(x, y, duration=0.1)
    py.click(x, y, button="left")
    time.sleep(1)

#DU
def dano():
    pdi.press('1')
    pdi.press('2')
    pdi.press('3')
    pdi.press('4')
    pdi.press('space')

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