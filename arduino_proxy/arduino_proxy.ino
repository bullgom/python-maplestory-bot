#include<Keyboard.h>
#include <Mouse.h>

#define PACKET_SIZE 2

#define COMMAND_INDEX 0
#define KEY_INDEX 1

#define KEY_PRESS 0
#define KEY_RELEASE 1
#define KEY_RELEASE_ALL 2
#define MOUSE_PRESS 3
#define MOUSE_RELEASE 4

byte packet_buffer[PACKET_SIZE];

void setup() {
  Serial.begin(9600);
  Keyboard.begin();
  Mouse.begin();
}

void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(packet_buffer, PACKET_SIZE);
    byte command = packet_buffer[COMMAND_INDEX];
    byte key = packet_buffer[KEY_INDEX];
    switch (command) {
      case KEY_PRESS:
      Keyboard.press(key);
      break;
      case KEY_RELEASE:
      Keyboard.release(key);
      break;
      case KEY_RELEASE_ALL:
      Keyboard.releaseAll();
      break;
      case MOUSE_PRESS:
      Mouse.press();
      break;
      case MOUSE_RELEASE:
      Mouse.release();
      break;
    }
  }
}
