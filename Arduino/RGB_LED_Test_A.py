#Test działania modułu RGB-LED KY-016 wesja Analog

import signal
from tkinter import *
from time import sleep
from PyMata.pymata import PyMata

# Podpięte piny Digital 9, 10, 11
blue = 11
red = 10
green = 9
pausa = 0.01
board = PyMata("/dev/ttyACM0", verbose=True)

# Ustawienie modułu piny blue, green, red PWM
board.set_pin_mode(blue, board.PWM, board.DIGITAL)
board.set_pin_mode(green, board.PWM, board.DIGITAL)
board.set_pin_mode(red, board.PWM, board.DIGITAL)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def rgb_led (pin, poz):
    board.analog_write(pin, poz)

for x in range(2):
    sleep(pausa)
    for li in range(255):
        rgb_led(blue,li)
        sleep(pausa)
    rgb_led(blue, 0)
    for li in range(255):
        rgb_led(red, li)
        sleep(pausa)
    rgb_led(red, 0)
    for li in range(255):
        rgb_led(green, li)
        sleep(pausa)
    rgb_led(green, 0)
    sleep(1)
board.close()
board.reset()
