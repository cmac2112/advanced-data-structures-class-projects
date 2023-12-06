#pos tester

import pyautogui
import pydirectinput as pd
from time import sleep

pyautogui.FAILSAFE = True

def main():
    nx = 630
    ny = 370

    pd.moveTo(nx, ny, duration = 1)

main()
