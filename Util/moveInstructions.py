import pyautogui as pygui
import time


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

def reset_camera():
    reset_char()
    time.sleep(1)
    pygui.moveTo(100, 100)
    pygui.keyDown("q")
    pygui.keyDown("left")
    while True:
        try:
            button7location = pygui.locateOnScreen('./Images/resetter.png',confidence = .55)
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
            button11location = pygui.locateCenterOnScreen('./Images/taskDone.png',confidence = .5)
            break
        except:
            pygui.click(1170,390)
            time.sleep(0.5)
            continue
    pygui.press("q")
    time.sleep(0.5)
    return
