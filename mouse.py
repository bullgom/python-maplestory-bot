#!/usr/bin/env python3

import serial

MOUSE_PRESS = 3
MOUSE_RELEASE = 4

class Mouse:
    def __init__(self, sio):
        self.sio = sio
        
    def _send(self, command):
        self.sio.write(bytearray([command, 0]))
        self.sio.flush()
        
    def press(self):
        self._send(MOUSE_PRESS)
        
    def release(self):
        self._send(MOUSE_RELEASE)

    def click(self):
        self.press()
        self.release()