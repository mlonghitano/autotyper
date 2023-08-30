import pyautogui
import time

def keep_awake():
    while True:
        pyautogui.typewrite('m')
        time.sleep(180)  # 3 minutes

if __name__ == "__main__":
    keep_awake()
#