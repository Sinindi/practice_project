import time
import pyautogui as pyg
import os

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
warn2 = pyg.locateCenterOnScreen(os.path.join(image_path , "warning2.png"))
if warn2 != None:
    pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "warning2.png")))
    pyg.move(150, -50)
    pyg.click()

warn = pyg.locateCenterOnScreen(os.path.join(image_path , "warning.png"))
if warn != None:
    pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "warning.png")))
    pyg.move(150, -100)
    pyg.click()
    time.sleep(0.5)
    pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "info.png")))
    pyg.move(420, -75)
    pyg.click()
    time.sleep(0.5)