#!/usr/bin/env python3

import pyautogui
import serial
import time

from key import *
from keyboard import Keyboard
from mouse import Mouse

def main():
    sio = serial.Serial('COM10', baudrate=9600)
    kb = Keyboard(sio)
    m = Mouse(sio)
    while True:
        m.click()
        m.release()
        kb.press(KEY_RETURN)
        kb.release(KEY_RETURN)
        kb.press(KEY_RETURN)
        kb.release(KEY_RETURN)
        time.sleep(0.8)
        
if __name__ == '__main__':
    main()