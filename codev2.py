import board
import keypad
import usb_hid
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# unused cuz can't see led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

KEY_PINS = (
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
)

BOTONS = {
    0: Keycode.F13,
    1: Keycode.F17,
    2: Keycode.F21,
    3: Keycode.F14,
    4: Keycode.F18,
    5: Keycode.F22,
    6: Keycode.F23,
    7: Keycode.F19,
    8: Keycode.F15,
    9: Keycode.F24,
    10: Keycode.F20,
    11: Keycode.F16,
}
    
keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)

while True:
    event = keys.events.get()
    if event:
        # A key transition occurred.

        if event.pressed:
            # Turn the key blue when pressed
            kbd.press(BOTONS[event.key_number])

        # This could just be else:,
        # since event.pressed and event.released are opposites.
        if event.released:
            kbd.release(BOTONS[event.key_number])
