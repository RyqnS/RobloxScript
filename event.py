import pyautogui as pygui
import time
from PIL import Image 
import numpy as np
import math
from pytesseract import pytesseract 
import re


#join event world, zoom out, and press Q. setup

def reset_char(): 
    pygui.press("esc")
    time.sleep(0.6)
    pygui.click(766,777)
    time.sleep(0.5)
    pygui.click(658,428)

def go_to_board(): #assumes character at reset area
    pygui.keyDown("w")
    time.sleep(3)
    pygui.keyUp("w")

def return_to_board(): 
    reset_char()
    go_to_board()

def open_board(): #assumes character in front of board
    pygui.keyUp("fn")
    while not task_done():
        if task_done():break
    pygui.click(721,474)
    time.sleep(.5)
    while not yes_no():
        if yes_no(): break
    pygui.click(1175,320)
    while not board_opened():
        if board_opened(): break

def get_tasks(): #assumes board is open
    im1 = pygui.screenshot(region=(273,209,310,40))
    im2 = pygui.screenshot(region=(600,209,310,40))
    im3 = pygui.screenshot(region=(929,209,310,40))
    text1 = pytesseract.image_to_string(im1).lstrip()
    text2 = pytesseract.image_to_string(im2).lstrip()
    text3 = pytesseract.image_to_string(im3).lstrip()
    outList = [text1,text2,text3]
    return outList

def yes_no():
    try:
        pygui.locateCenterOnScreen('yesno.png',confidence = .7)
        return True
    except:
        return False

def board_opened():
    try:
        pygui.locateCenterOnScreen('boardOpened.png',confidence = .7)
        return True
    except:
        return False

def do_task():
    open_board()
    outList = get_tasks()
    while "Pizza Deliverv\n" not in outList and "Making Pizza\n" not in outList:
        #accept first quest
        pygui.click(440,350)
        while not yes_no():
            if yes_no(): break
        pygui.click(1175,320)
        time.sleep(1)
        while not task_done():
            pygui.click(1175,320)
            if task_done(): break

        #give up quest
        open_board()
        outList = get_tasks()

    if "Making Pizza\n" in outList:
        pygui.click(425,425) 
        time.sleep(1.25) #do u want to accept this quest?
        pygui.click(1175,320)
        time.sleep(1.25)
        pygui.click(1175,320)
        time.sleep(.1)
        pygui.click(1175,320)
        time.sleep(0.5)
        make_pizza()

    elif "Pizza Deliverv\n" in outList:
        pygui.click(425,425)
        time.sleep(1)
        pygui.click(1175,320)
        time.sleep(1)
        pygui.click(1175,320)
        time.sleep(1)
        pizza_delivery()  

    # elif "Package Deliverv\n" in outList:
    #     pygui.click(425,425) 
    #     time.sleep(1) #do u want to accept this quest?
    #     pygui.click(1175,320) 
    #     time.sleep(1) #pick up pacakge from
    #     im1 = pygui.screenshot(region=(200,100,1000,130))
    #     text1 = pytesseract.image_to_string(im1).lstrip()
    #     x = re.findall(r'\d+', text1)
    #     houseNum = int(x[-1])
    #     pygui.click(1175,320)
    #     time.sleep(0.5)
    #     package_delivery(houseNum)
    
    

def navigate_to_house(num): #assumes at spawn
    pygui.keyUp("fn")
    mapX = {16: 1.525, 15:2.2, 14:2.83,12:3.5}
    if num in {1,2,3,4,5}:
        pygui.keyDown("d")
        time.sleep(0.1)
        pygui.keyUp("d")
        pygui.keyDown("w")
        time.sleep(3)
        pygui.keyUp("w")
        turn_around()
        pygui.keyDown("a")
        if num == 1:
            time.sleep(1.5)
        elif num ==2:
            time.sleep(2.2)
        elif num ==3:
            time.sleep(2.8)
        elif num ==4:
            time.sleep(4)
        else:
            time.sleep(5.05)
        pygui.keyUp("a")
        pygui.keyDown("w")
        time.sleep(0.75)
        pygui.keyUp("w")
        # pygui.click(700,375)
    elif num == 13:
        pygui.keyDown("d")
        time.sleep(1.75)
        pygui.keyUp("d")
        pygui.keyDown("w")
        time.sleep(0.5)
        pygui.keyUp("w")
    elif num in {16,15,14,12}:
        pygui.keyDown("d")
        time.sleep(mapX[num])
        pygui.keyUp("d")
        turn_around()
        pygui.keyDown("w")
        time.sleep(0.5)
        pygui.keyUp("w")
    elif num in {8,7,6,10}:
        pygui.keyDown("d")
        time.sleep(4.85)
        pygui.keyUp("d")
        if num == 10:
            pygui.keyDown("s")
            time.sleep(0.5)
            pygui.keyUp("s")
            turn_quarter_left()
            pygui.keyDown("w")
            time.sleep(1)
            pygui.keyUp("w")
        elif num == 8:
            turn_quarter_right()
            pygui.keyUp("fn")
            pygui.keyDown("d")
            time.sleep(0.115)
            pygui.keyUp("d")
            pygui.keyDown("w")
            time.sleep(0.6)
            pygui.keyUp("w")
        else:
            if num == 6:
                pygui.keyDown("w")
                time.sleep(0.8)
                pygui.keyUp("w")
                turn_quarter_right()
            elif num == 7:
                pygui.keyDown("w")
                time.sleep(0.675)
                pygui.keyUp("w")
                turn_quarter_left()
            pygui.keyDown("w")
            time.sleep(0.9)
            pygui.keyUp("w")

    elif num in {9,11}:
        pygui.keyDown("d")
        time.sleep(3.5)
        pygui.keyUp("d")
        if num == 9:
            pygui.keyDown("w")
            time.sleep(0.36)
            pygui.keyUp("w")
            turn_quarter_left()
        else:
            pygui.keyDown("w")
            time.sleep(0.8)
            pygui.keyUp("w")
            turn_quarter_left()
        pygui.keyDown("w")
        time.sleep(0.6)
        pygui.keyUp("w")    

def turn_around():
    pygui.keyDown("left")
    time.sleep(1.39)
    pygui.keyUp("left")

def turn_quarter_left():
    pygui.keyDown("left")
    time.sleep(.68)
    pygui.keyUp("left")

def turn_quarter_right():
    pygui.keyDown("right")
    time.sleep(.68)
    pygui.keyUp("right")

def make_pizza(): #assumes in front of board
    pygui.keyDown("a")
    pygui.keyDown("w")
    time.sleep(1.6)
    pygui.keyUp("fn")
    pygui.keyUp("a")
    pygui.keyUp("w")
    time.sleep(0.2)
    pygui.keyDown("d")
    time.sleep(0.125)
    pygui.keyUp("d")
    pygui.keyDown("w")
    time.sleep(0.05)
    pygui.keyUp("w")
    pygui.keyDown("a")
    time.sleep(0.5)
    pygui.keyUp("a")
    time.sleep(1)
    while True:
        try:
            button11location = pygui.locateCenterOnScreen('enteredPizzaria.png',confidence = .5)
            break
        except:
            continue
    time.sleep(0.1)
    pygui.keyDown("w")
    time.sleep(2)
    pygui.keyDown("a")
    time.sleep(1)
    pygui.keyUp("w")
    pygui.keyUp("a")
    i=0
    while True:
        if chef2_clicked():
            break
        else:
            pygui.click(675+10*i,490)
            if chef2_clicked(): break
            pygui.click(675-10*i,490)
            if chef2_clicked(): break
            pygui.click(675,490+10*i)
            if chef2_clicked(): break
            pygui.click(675,490-10*i)
            if chef2_clicked(): break
            i+=1
    time.sleep(0.5)
    pygui.click(1170,320) 
    time.sleep(1.25)
    pygui.click(1170,320) 
    time.sleep(1.25)
    pygui.click(1170,320) 
    time.sleep(6)
    pygui.click(1170,320)
    time.sleep(2)
    wants = []
    wantsDict = {"cheese":(472,262),"sauce":(980,230),"pineapple":(1120,350),"mushroom":(380,440),"parsley":(230,530),"sausage":(1145,515),"chicken":(1280,630),"pepperoni":(360,610),"jalapeno":(1260,410),"onion":(250,350)}
    im1 = pygui.screenshot(region=(200,100,1000,130))
    text1 = pytesseract.image_to_string(im1).lstrip()
    if "no cheese" in text1:
        pass
    elif "cheese" in text1:
        wants.append("cheese")
    if "not" in text1 and "sauce" in text1:
        pass
    elif "sauce" in text1:
        wants.append("sauce")
    time.sleep(0.2)
    pygui.click(1170,320)
    time.sleep(2)
    im2 = pygui.screenshot(region=(200,100,1000,130))
    text2 = pytesseract.image_to_string(im2).lstrip().lower().replace(',', '').replace('.','')
    for word in text2.split():
        if word in wantsDict.keys():
            wants.append(word)
    time.sleep(0.5)
    pygui.click(1170,320)
    time.sleep(1.5)
    for topping in wants:
        pygui.click(wantsDict[topping])
        time.sleep(0.5)
    pygui.click(750,800)
    while not task_done():
        pygui.click(1170,320)
        if task_done(): break
        pygui.click(1170,320)
        if task_done(): break
    reset_char()
    time.sleep(0.5)
    pygui.keyDown("s")
    time.sleep(0.5)
    pygui.keyUp("s")
    time.sleep(1)
    while True:
        try:
            button11location = pygui.locateCenterOnScreen('leftPizzaria.png',confidence = .2)
            break
        except:
            continue
    time.sleep(0.1)
    pygui.press("q")
    time.sleep(0.1)

def pizza_delivery(): #assumes in front of board
    pygui.keyDown("a")
    pygui.keyDown("w")
    time.sleep(1.6)
    pygui.keyUp("fn")
    pygui.keyUp("a")
    pygui.keyUp("w")
    time.sleep(0.2)
    pygui.keyDown("d")
    time.sleep(0.125)
    pygui.keyUp("d")
    pygui.keyDown("w")
    time.sleep(0.185)
    pygui.keyUp("w")
    i = 0
    while not chef_clicked():
        pygui.click(420+35*i,480-20*i)
        time.sleep(1)
        if chef_clicked(): break
        pygui.click(420-35*i,480+20*i)
        time.sleep(1)
        if chef_clicked(): break
        i+=1
    time.sleep(.5)
    pygui.click(1170,390)
    time.sleep(1)
    pygui.click(1170,390)
    time.sleep(1)
    pygui.click(1170,390) 
    time.sleep(1.5)
    im1 = pygui.screenshot(region=(200,100,1000,130))
    text1 = pytesseract.image_to_string(im1).lstrip()
    x = re.findall(r'\d+', text1)
    if x == []:
        x = []
        pygui.click(420+35*i,480-20*i)
        time.sleep(1.5)
        im1 = pygui.screenshot(region=(200,100,1000,130))
        text1 = pytesseract.image_to_string(im1).lstrip()
        x = re.findall(r'\d+', text1)
        pygui.click(420+35*i,480-20*i)
        time.sleep(0.5)
        if x!= []: pass
        pygui.click(420-35*i,480+20*i)
        time.sleep(1.5)
        im1 = pygui.screenshot(region=(200,100,1000,130))
        text1 = pytesseract.image_to_string(im1).lstrip()
        x = re.findall(r'\d+', text1)
        pygui.click(420-35*i,480+20*i)
        time.sleep(0.5)
    houseNum = int(x[-1])
    pygui.click(1170,390)
    time.sleep(1)
    reset_char()
    while not task_done():
        continue
    navigate_to_house(houseNum)
    time.sleep(0.5)
    i=0
    yStart = 375
    if houseNum == 4 or houseNum == 5:
        yStart = 455
    while not house_clicked():
        pygui.click(760+20*i,yStart)
        time.sleep(1)
        if house_clicked(): break
        pygui.click(760-20*i,yStart)
        time.sleep(1)
        if house_clicked(): break
        pygui.click(760+10*i,yStart+40*i)
        time.sleep(1)
        if house_clicked(): break
        pygui.click(760-10*i,yStart-40*i)
        time.sleep(1)
        if house_clicked(): break
        i+=1
        if i > 5:
            reset_camera()
            time.sleep(1.5)
            navigate_to_house(houseNum)
            time.sleep(0.5)
            i = 0
    time.sleep(0.5)
    pygui.click(1170,390) 
    time.sleep(1)
    while not task_done():
        pygui.click((1170,390))
        time.sleep(0.5)
    time.sleep(0.4)
    pygui.click(1170,390)
    time.sleep(0.1)
    pygui.keyUp("fn")

def task_done():
    try:
        pygui.locateCenterOnScreen('taskDone.png',confidence = .7)
        return True
    except:
        return False
    
    
def house_clicked():
    try:
        pygui.locateCenterOnScreen('houseClicked.png',confidence = 0.9)
        return True
    except:
        return False
    
def chef_clicked():
    try:
        pygui.locateCenterOnScreen('chefClicked.png',confidence = .6)
        return True
    except:
        return False
    
def chef2_clicked():
    try:
        pygui.locateCenterOnScreen('chef2Clicked.png',confidence = .4)
        return True
    except:
        return False

def package_delivery(num): #assumes in front of board
    reset_char()
    time.sleep(1.5)
    navigate_to_house(num)
    i = 0
    while True:
        if house_clicked():
            break
        else:
            pygui.click(760+10*i,375)
            if house_clicked(): break
            pygui.click(760-10*i,375)
            if house_clicked(): break
            pygui.click(760+10*i,375+20*i)
            if house_clicked(): break
            pygui.click(760-10*i,375-20*i)
            if house_clicked(): break
            i+=1
    time.sleep(2)
    im1 = pygui.screenshot(region=(200,100,1000,130))
    text1 = pytesseract.image_to_string(im1).lstrip()
    x = re.findall(r'\d+', text1)
    houseNum = int(x[-1])
    pygui.click(1170,390)
    time.sleep(2)
    pygui.click(1170,390)
    time.sleep(1)
    reset_camera()
    time.sleep(1.5)
    navigate_to_house(houseNum)
    i=0
    while True:
        if house_clicked():
            break
        else:
            pygui.click(760+10*i,375)
            if house_clicked(): break
            pygui.click(760-10*i,375)
            if house_clicked(): break
            pygui.click(760+10*i,375+20*i)
            if house_clicked(): break
            pygui.click(760-10*i,375-20*i)
            if house_clicked(): break
            i+=1
    time.sleep(2)
    pygui.click(1170,390)
    time.sleep(2)
    pygui.click(1170,390)
    time.sleep(1)
    pygui.click(1170,390)
    time.sleep(0.5)

def train_clicked():
    try:
        pygui.locateCenterOnScreen('trainClicked.png',confidence = .7)
        return True
    except:
        return False

def reset_camera():
    reset_char()
    time.sleep(1)
    pygui.moveTo(100, 100)
    pygui.keyDown("q")
    pygui.keyDown("left")
    while True:
        try:
            button7location = pygui.locateOnScreen('resetter.png',confidence = .55)
        except:
            continue
        else:
            break
    pygui.keyUp("left")
    pygui.keyDown("right")
    time.sleep(0.35)
    pygui.keyUp("right")
    pygui.keyDown("w")
    time.sleep(0.3)
    pygui.keyUp("w")
    i = 0
    pygui.keyUp("fn")
    while not yes_no():
        pygui.click(760-40*i,460)
        if yes_no():break
        pygui.click(760+40*i,460)
        if yes_no():break
        i+=1
    pygui.click(1170,330)
    time.sleep(3)
    pygui.click(1170,390)
    time.sleep(2)
    pygui.click(1170,390)
    time.sleep(1.5)
    pygui.click(1170,390)
    time.sleep(0.5)
    while True:
        try:
            button11location = pygui.locateCenterOnScreen('taskDone.png',confidence = .5)
            break
        except:
            pygui.click(1170,390)
            time.sleep(0.5)
            continue
    pygui.press("q")
    time.sleep(0.5)
    return

if __name__ == "__main__":
    time.sleep(3)
    while True:    
        go_to_board()
        do_task()
        time.sleep(0.3)
        reset_camera()
    # reset_camera()
    # go_to_board()
    # do_task()

