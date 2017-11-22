# Test LCD 1602 piny SDA A1, SCL A0

import sys
import signal
from time import sleep

from PyMata.pymata import PyMata

scl = 0
sda = 1

board = PyMata("/dev/ttyACM0", verbose=True)

board.i2c_config(0, board.ANALOG, 0, 1)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)
board.i2c_write(0x27, 1, 1, 1)
sleep(2)
print("Test")
sleep(2)
print("Koniec")

signal.signal(signal.SIGINT, signal_handler)

board.close()

# Porzucony temat