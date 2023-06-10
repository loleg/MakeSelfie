# MakeZurich Badge 2023

# Requires:
#  lib/neopixel.mpy


import time
import board
import busio
import microcontroller
from rainbowio import colorwheel
import neopixel
import digitalio
import touchio
import binascii
import usb_cdc

uart = busio.UART(board.GP4, board.GP5, baudrate=9600, timeout=20)

usb_cdc.data.write(b"federico_vanzati")

pixel_pin = board.GP22
num_pixels = 6
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

tp1 = touchio.TouchIn(board.GP9)
tp2 = touchio.TouchIn(board.GP19)

btn = digitalio.DigitalInOut(board.GP6)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

def at_send(cmd, max_time=10):
    if not isinstance(cmd, bytes):
        print("cmd must be a byte string, terminated with new line")
        return ""

    now = time.monotonic()
    uart.write(cmd)
    result = ""
    while True:
        byte_read = uart.readline() # read one line
        if byte_read == None: # no more response
            break

        response = byte_read.decode()
        result += response
        if (time.monotonic() - now) > max_time:
            print("reached at_send max_time", max_time)
            break

    return result

# return dict with the ids
def lora_get_ids():
    response = at_send(b"AT+ID\n")
    result = {
        "DevAddr": "",
        "DevEui": "",
        "AppEui": "",
    }
    for line in response.splitlines():
        for key in result.keys():
            if key in line:
                result[key] = line.split(",")[1].strip()

    return result

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
BLACK = (0, 0, 0)
effects = [RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, BLACK]

previous_state = btn.value
current_effect = 0
tp1_prev = False

uid = binascii.hexlify(microcontroller.cpu.uid)
lora_ids = lora_get_ids()

rainbow_cycle(0)

while True:
    print("federico_vanzati")
    if(tp1.value == True and tp1_prev == False):
        # TP1 button pressed
        usb_cdc.data.write(uid)
        #for name, id in lora_ids.items():
        #    usb_cdc.data.write(f"{name}: {id}")
        #usb_cdc.data.write('\n')
        tp1_prev = True
    elif(tp1.value == False and tp1_prev == True):
        # TP1 button released
        tp1_prev = False
    
    current_state = btn.value
    if current_state != previous_state:
        if not current_state:
            print("Button is down")
        else:
            print("Button is up")
            color_chase(effects[current_effect], 0.1)  # Increase the number to slow down the color chase
            current_effect = current_effect + 1
            print(current_effect, len(effects))
            if current_effect >= len(effects):
                current_effect = 0

    previous_state = current_state
