#!/usr/bin/env python3

import serial

KEY_PRESS = 0
KEY_RELEASE = 1
KEY_RELEASE_ALL = 2

class Keyboard:
    def __init__(self, sio):
        self.sio = sio
                            
    def _send(self, command, key):
        self.sio.write(bytearray([command, key]))
        self.sio.flush()
                            
    def press(self, key):
        self._send(KEY_PRESS, key)
        
    def release(self, key):
        self._send(KEY_RELEASE, key)
        
    def releaseAll(self):
        self._send(KEY_RELEASE_ALL, 0)

    def type(self, key):
        self.press(key)
        self.release(key)