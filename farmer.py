import pyautogui
import keyboard
import concurrent.futures
import time

actualImage=''

def matchImage(imgs):
    with concurrent.futures.ThreadPoolExecutor() as exec:
         return exec.map(find,imgs)

def find(img):
    global actualImage
    start = pyautogui.locateOnScreen(img,grayscale=False,confidence=0.80)
    if (start) is not None:
        if(img != './coins/cancel-join.png'):
            x,y=pyautogui.center(start)
            pyautogui.click(x,y)
            actualImage= img 

def searchQuest():
    global actualImage
    actualImage=''
    print("search")
    imgSet=['./coins/select-quest.png','./coins/select-quest2.png','./coins/join-room.png','./coins/join-room2.png','./coins/ready.png','./coins/no-rooms.png','./coins/close.png']
    match=matchImage(imgSet)
    print(actualImage)
    while (actualImage != './coins/ready.png'):
        if(actualImage=='./coins/no-rooms.png'):
            pyautogui.click(1407,220)
            actualImage=''
        time.sleep(1)
        match=matchImage(imgSet)
        print(actualImage)
    time.sleep(20)
    continueQuest()

def continueQuest():
    global actualImage
    actualImage=''
    print("continue quest")
    imgSet=['./coins/continue1.png','./coins/continue2.png','./coins/retry.png','./coins/cancel-join.png','./coins/close.png']
    match=matchImage(imgSet)
    while(actualImage == './coins/cancel-join.png' or actualImage == ''):
        time.sleep(20)
        match=matchImage(imgSet)
        print(actualImage)
    while(actualImage != './coins/retry.png'):
        match=matchImage(imgSet)
        print(actualImage)
    searchQuest()

searchQuest()
