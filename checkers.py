import pyautogui as pygui


def train_clicked():
    try:
        pygui.locateCenterOnScreen('./Images/trainClicked.png',confidence = .7)
        return True
    except:
        return False

def yes_no():
    try:
        pygui.locateCenterOnScreen('./Images/yesno.png',confidence = .7)
        return True
    except:
        return False

def board_opened():
    try:
        pygui.locateCenterOnScreen('./Images/boardOpened.png',confidence = .7)
        return True
    except:
        return False
    
def task_done():
    try:
        pygui.locateCenterOnScreen('./Images/taskDone.png',confidence = .7)
        return True
    except:
        return False
    
    
def house_clicked():
    try:
        pygui.locateCenterOnScreen('./Images/houseClicked.png',confidence = 0.9)
        return True
    except:
        return False
    
def chef_clicked():
    try:
        pygui.locateCenterOnScreen('./Images/chefClicked.png',confidence = .6)
        return True
    except:
        return False
    
def chef2_clicked():
    try:
        pygui.locateCenterOnScreen('./Images/chef2Clicked.png',confidence = .4)
        return True
    except:
        return False