import pyautogui as pygui
import time
from PIL import Image 
import numpy as np
import math
from pytesseract import pytesseract 
import re


def run_except(doodle): #assumes in battle
    im1 = pygui.screenshot(region=(175,205,250,40))
    text1 = pytesseract.image_to_string(im1).lstrip()
    print(text1)
    if text1 != doodle and text1 != "Pandishi" and text1 != "Qilintel":
        pygui.click(1210,750)

def in_battle():
    try:
        pygui.locateCenterOnScreen('options.png',confidence = 0.9)
        return True
    except:
        return False

if __name__ == "__main__":
    time.sleep(3)
    while True:
        if in_battle():
            run_except("Threasant")
        else:
            continue
