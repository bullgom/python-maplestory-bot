#import <Keyboard.h>

#define PACKET_SIZE 2

#define COMMAND_INDEX 0
#define KEY_INDEX 1

#define PRESS_COMMAND 0
#define RELEASE_COMMAND 1
#define RELEASE_ALL_COMMAND 2

byte packet_buffer[PACKET_SIZE];

void setup() {
  Serial.begin(9600);
  Keyboard.begin();
}

void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(packet_buffer, PACKET_SIZE);
    byte command = packet_buffer[COMMAND_INDEX];
    byte key = packet_buffer[KEY_INDEX];
    switch (command) {
      case PRESS_COMMAND:
      Keyboard.press(key);
      break;
      case RELEASE_COMMAND:
      Keyboard.release(key);
      break;
      case RELEASE_ALL_COMMAND:
      Keyboard.releaseAll();
    }
    Serial.println("Pressing " + key);
  }
}
