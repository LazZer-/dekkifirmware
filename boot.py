# this is a sort of devmode, if you press two buttons during boot,
# you can access the files on the pico, otherwise it won't show up
# as a flash drive
import board
import time
import digitalio
import storage

# defining pins to buttons

b1p = board.GP10
b10p = board.GP19

b1 = digitalio.DigitalInOut(b1p)
b1.direction = digitalio.Direction.INPUT
b1.pull = digitalio.Pull.UP

b10 = digitalio.DigitalInOut(b10p)
b10.direction = digitalio.Direction.INPUT
b10.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# check if the button combo is pressed

if b1.value and b10.value:
    storage.disable_usb_drive()
else:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    led.value = True
