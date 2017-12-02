#Test działania modułu RGB-LED KY-016 wesja Analog

import sys
import signal
from tkinter import *
from PyMata.pymata import PyMata

# Podpięte piny Digital 9, 10, 11
blue = 11
red = 10
green = 9
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


def rd(val):
    rgb_led(red, int(val))
def gr(val):
    rgb_led(green, int(val))
def bl(val):
    rgb_led(blue, int(val))

master = Tk()
r = Scale(master, from_=0, to=255, command=(rd))
r.pack()
g = Scale(master, from_=0, to=255,command=(gr))
g.pack()
b = Scale(master, from_=0, to=255, command=(bl))
b.pack()

mainloop()


board.close()
board.reset()
