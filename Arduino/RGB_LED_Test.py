#Test działania modułu RGB-LED KY-016 wesja Digital



import sys
import signal
from time import sleep

from PyMata.pymata import PyMata

# Podpięte piny Digital 3,4,5

blue = 3
green = 4
red = 5
pausa = 0.3



board = PyMata("/dev/ttyACM0", verbose=True)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Ustawienie modułu piny blue, green, red Output


board.set_pin_mode(blue, board.OUTPUT, board.DIGITAL)
board.set_pin_mode(green, board.OUTPUT, board.DIGITAL)
board.set_pin_mode(red, board.OUTPUT, board.DIGITAL)


for x in range(10):
    sleep(pausa)
    board.digital_write(blue, 1)
    sleep(pausa)
    board.digital_write(blue, 0)
    sleep(pausa)
    board.digital_write(green, 1)
    sleep(pausa)
    board.digital_write(green, 0)
    sleep(pausa)
    board.digital_write(red, 1)
    sleep(pausa)
    board.digital_write(red, 0)

board.close()
