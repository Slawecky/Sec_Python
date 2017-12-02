#Test działania modułu RGB-LED KY-016 wesja Analog

import sys
import signal
from tkinter import *
from PyMata.pymata import PyMata

# Podpięte piny Digital 9, 10, 11
blue = 11
red = 9
green = 10
#board = PyMata("/dev/ttyACM0", verbose=True)
board = PyMata("\.\COM4", verbose=True)
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

def rd(val):
    board.analog_write(red, int(val))
def gr(val):
    board.analog_write(green, int(val))
def bl(val):
    board.analog_write(blue, int(val))

master = Tk()
master.title("RGB LED")
master.geometry('250x200')

r = Scale(master, from_=255, to=0, command=(rd), label="Red", troughcolor="red")
r.pack(side=LEFT)
g = Scale(master, from_=255, to=0,command=(gr), label="Green", troughcolor="green")
g.pack(side=RIGHT)
b = Scale(master, from_=255, to=0, command=(bl), label="Blue", troughcolor="blue")
b.pack(side=RIGHT)

mainloop()


board.close()
board.reset()
