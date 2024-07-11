import pyautogui
import time

count = 1
while True:
    if count % 2:
        pyautogui.moveTo(100, 100)
    else:
        pyautogui.moveTo(200, 200)
    time.sleep(60)
    count += 1
