import board
import time
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# defining pins

b1p = board.GP10
b2p = board.GP11
b3p = board.GP12
b4p = board.GP13
b5p = board.GP14
b6p = board.GP15
b7p = board.GP16
b8p = board.GP17
b9p = board.GP18
b10p = board.GP19
b11p = board.GP20
b12p = board.GP21

# initializing buttons

b1 = digitalio.DigitalInOut(b1p)
b1.direction = digitalio.Direction.INPUT
b1.pull = digitalio.Pull.UP

b2 = digitalio.DigitalInOut(b2p)
b2.direction = digitalio.Direction.INPUT
b2.pull = digitalio.Pull.UP

b3 = digitalio.DigitalInOut(b3p)
b3.direction = digitalio.Direction.INPUT
b3.pull = digitalio.Pull.UP

b4 = digitalio.DigitalInOut(b4p)
b4.direction = digitalio.Direction.INPUT
b4.pull = digitalio.Pull.UP

b5 = digitalio.DigitalInOut(b5p)
b5.direction = digitalio.Direction.INPUT
b5.pull = digitalio.Pull.UP

b6 = digitalio.DigitalInOut(b6p)
b6.direction = digitalio.Direction.INPUT
b6.pull = digitalio.Pull.UP

b7 = digitalio.DigitalInOut(b7p)
b7.direction = digitalio.Direction.INPUT
b7.pull = digitalio.Pull.UP

b8 = digitalio.DigitalInOut(b8p)
b8.direction = digitalio.Direction.INPUT
b8.pull = digitalio.Pull.UP

b9 = digitalio.DigitalInOut(b9p)
b9.direction = digitalio.Direction.INPUT
b9.pull = digitalio.Pull.UP

b10 = digitalio.DigitalInOut(b10p)
b10.direction = digitalio.Direction.INPUT
b10.pull = digitalio.Pull.UP

b11 = digitalio.DigitalInOut(b11p)
b11.direction = digitalio.Direction.INPUT
b11.pull = digitalio.Pull.UP

b12 = digitalio.DigitalInOut(b12p)
b12.direction = digitalio.Direction.INPUT
b12.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Blink led to confirm initialization, then keep it on

led.value = True
time.sleep(0.3)
led.value = False
time.sleep(0.2)
led.value = True
time.sleep(0.3)
led.value = False
time.sleep(0.2)
led.value = True


# Check if something is pressed and hit that key.
# Change the Keycode.* part if you want another key, replace * with preferred key.
# Keylist: https://circuitpython.readthedocs.io/
#           projects/hid/en/latest/_modules/adafruit_hid/keycode.html#Keycode
# You can also chain several keys with commas, e.g. kbd.send(Keycode.CONTROL, Keycode.C)

while True:
    if not b1.value:
        kbd.press(Keycode.F13)
    else:
        kbd.release(Keycode.F13)
    if not b2.value:
        kbd.press(Keycode.F17)
    else:
        kbd.release(Keycode.F17)
    if not b3.value:
        kbd.press(Keycode.F21)
    else:
        kbd.release(Keycode.F21)
    if not b4.value:
        kbd.press(Keycode.F14)
    else:
        kbd.release(Keycode.F14)
    if not b5.value:
        kbd.press(Keycode.F18)
    else:
        kbd.release(Keycode.F18)
    if not b6.value:
        kbd.press(Keycode.F22)
    else:
        kbd.release(Keycode.F22)
    if not b7.value:
        kbd.press(Keycode.F23)
    else:
        kbd.release(Keycode.F23)
    if not b8.value:
        kbd.press(Keycode.F19)
    else:
        kbd.release(Keycode.F19)
    if not b9.value:
        kbd.press(Keycode.F15)
    else:
        kbd.release(Keycode.F15)
    if not b10.value:
        kbd.press(Keycode.F24)
    else:
        kbd.release(Keycode.F24)
    if not b11.value:
        kbd.press(Keycode.F20)
    else:
        kbd.release(Keycode.F20)
    if not b12.value:
        kbd.press(Keycode.F16)
    else:
        kbd.release(Keycode.F16)
    time.sleep(0.008)
# Write your code here :-)
