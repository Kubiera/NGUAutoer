import time
import keyboard
import pyautogui

WIDTH, HEIGHT = pyautogui.size()

time.sleep(5)

cube = pyautogui.locateCenterOnScreen("images/cube.PNG", grayscale=True, confidence= 0.9)
if cube is None:
    print("could not find cube location")
    exit()

while not keyboard.is_pressed('q'):
    pyautogui.moveTo(cube)
    pyautogui.click(button='right', clicks=2, interval=0.25)
    fruit = pyautogui.locateCenterOnScreen(image="images/fruitReady.PNG", confidence= 0.9)
    pit = pyautogui.locateCenterOnScreen(image= "images/moneyPit.PNG", confidence=0.9)
    magic = pyautogui.locateCenterOnScreen(image="images/bloodMagic.PNG", confidence=0.9)
    
    if fruit is not None:
        pyautogui.moveTo(fruit)
        pyautogui.leftClick()
        harvest = pyautogui.locateCenterOnScreen("images/harvestFruit.PNG", grayscale=True, confidence= 0.9)
        pyautogui.moveTo(harvest)
        pyautogui.leftClick()
        inventory = pyautogui.locateCenterOnScreen("images/inventory.PNG", grayscale=True, confidence= 0.9)
        pyautogui.moveTo(inventory)
        pyautogui.leftClick()

    if magic is not None:
        pyautogui.moveTo(magic)
        pyautogui.leftClick()
        spells = pyautogui.locateCenterOnScreen(image="images/spellList.PNG", grayscale=True, confidence= 0.9)
        pyautogui.moveTo(spells)
        pyautogui.leftClick()
        ironPill = pyautogui.locateCenterOnScreen(image="images/ironPill.PNG", grayscale=True, confidence= 0.9)
        pyautogui.moveTo(ironPill)
        pyautogui.leftClick()
        inventory = pyautogui.locateCenterOnScreen("images/inventory.PNG", grayscale=True, confidence= 0.9)
        pyautogui.moveTo(inventory)
        pyautogui.leftClick()

    time.sleep(5)