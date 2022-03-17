import pyautogui as pyg
import os

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")


    
pyg.click()
pyg.press('down')
pyg.hotkey('shift', 'f10')