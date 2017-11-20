#Test działania modułu Arduino KY-038 Microphone sound sensor


import sys
import signal
from time import sleep

from PyMata.pymata import PyMata

analog_out = 0
digital_sw = 6

board = PyMata("/dev/ttyACM0", verbose=True)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Ustawienie modułu Pin A0 analog, D6 On\Off

board.set_pin_mode(analog_out, board.INPUT, board.ANALOG)
board.set_pin_mode(digital_sw, board.INPUT, board.DIGITAL)
board.digital_write(digital_sw, 1)

for x in range(100):
    status = board.analog_read(analog_out)
    #print(f"{x + 1}, przebieg")
    print(status)
    sleep(.01)
#board.digital_write(digital_sw, 0)
board.close()
