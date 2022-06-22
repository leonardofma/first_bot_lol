import pyautogui
from time import sleep

def click(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()

def check_screen():
    sleep(2)
    button_pos = pyautogui.locateOnScreen('image_lol.png', confidence=0.7)
    if button_pos != None:
        click(button_pos.left, button_pos.top)
        return True
    return False
def send_email():
    pass

def main():
    while True:
      if  check_screen():
        print('aceitei a partida')
        sleep(6)
main()

