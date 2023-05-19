from pyfirmata import Arduino,SERVO
from time import sleep

port = 'COM3'
board = Arduino(port)

redLed = 5
yeLed = 3
greenLed = 4

board.digital[redLed].write(1)
board.digital[greenLed].write(1)
board.digital[yeLed].write(1)

sleep(2)

board.digital[redLed].write(0)
board.digital[greenLed].write(0)
board.digital[yeLed].write(0)