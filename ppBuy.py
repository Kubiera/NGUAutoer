import time
import keyboard
import pyautogui

buy = pyautogui.locateCenterOnScreen("images/PPBuy.PNG", grayscale=True, confidence= 0.9)
pyautogui.moveTo(buy)
pyautogui.leftClick()
time.sleep(0.05)
confirm = pyautogui.locateCenterOnScreen("images/Confirm.PNG", grayscale=True, confidence=0.9)
pyautogui.moveTo(confirm)
pyautogui.leftClick()
time.sleep(0.05)

while not keyboard.is_pressed("q"):
    pyautogui.moveTo(buy)
    pyautogui.leftClick()
    time.sleep(0.05)
    pyautogui.moveTo(confirm)
    pyautogui.leftClick()
    time.sleep(0.05)