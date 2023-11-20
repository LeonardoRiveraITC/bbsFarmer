import pyautogui
import keyboard
import concurrent.futures
import time

def find(img):
    start = pyautogui.locateOnScreen(img,grayscale=True,confidence=0.70)
    if (start) is not None:
        x,y=pyautogui.center(start)
        pyautogui.click(x,y)
        if (img=='./images/ready.png'):
            time.sleep(120)
        if(img=='./images/no-rooms.png'):
            pyautogui.click(1630,223)

imgs=['./images/no-rooms.png','./images/select.png','./images/join.png','./images/ready.png','./images/close.png','./images/continue2.png','./images/continue.png','./images/retry.png']
while not keyboard.is_pressed('q'):
    with concurrent.futures.ThreadPoolExecutor() as exec:
        guix=exec.map(find,imgs)
    time.sleep(2)
 #   if guix is not None:
