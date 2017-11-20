#Test działania modułu RGB-LED KY-016 wesja Analog



import sys
import signal
from time import sleep

from PyMata.pymata import PyMata

# Podpięte piny Digital 9, 10, 11

blue = 9
red = 10
green = 11
pausa = 0.01




board = PyMata("/dev/ttyACM0", verbose=True)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C')
    if board is not None:
        board.reset()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Ustawienie modułu piny blue, green, red PWM


board.set_pin_mode(blue, board.PWM, board.DIGITAL)
board.set_pin_mode(green, board.PWM, board.DIGITAL)
board.set_pin_mode(red, board.PWM, board.DIGITAL)


for x in range(2):
    sleep(pausa)
    for li in range(255):
        board.analog_write(blue, li)
        sleep(pausa)
    board.analog_write(blue, 0)
    for li in range(255):
        board.analog_write(red, li)
        sleep(pausa)
    board.analog_write(red, 0)
    for li in range(255):
        board.analog_write(green, li)
        sleep(pausa)
    board.analog_write(green, 0)
    sleep(1)
board.close()
board.reset()
