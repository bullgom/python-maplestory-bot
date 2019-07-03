#!/usr/bin/env python3

from key import *

import serial

PRESS_COMMAND = 0
RELEASE_COMMAND = 1
RELEASE_ALL_COMMAND = 2

class Keyboard:
    def __init__(self, serial_location, baudrate=9600):
        self.serial = serial.Serial(serial_location,
                                    baudrate)
                            
    def _send_command(self, command, key):
        self.serial.write(bytearray([command, key]))
        self.serial.flush()
                            
    def press(self, key):
        self._send_command(PRESS_COMMAND, key)
        
    def release(self, key):
        self._send_command(RELEASE_COMMAND, key)
        
    def releaseAll(self):
        self._send_command(RELEASE_ALL_COMMAND, 0)

def main():
    kb = Keyboard('COM9')
    import time
    time.sleep(2)
    kb.press(KEY_LEFT_CTRL)
    kb.press(ord('c'))
    kb.releaseAll()

if __name__ == '__main__':
    main()