from gpiozero import LEDBoard
import time

star = LEDBoard(2, pwm=True)
star.on()

tree = LEDBoard(*range(4,28),pwm=True)

while True:
    for ledid in range(12):
        tree[ledid].on()
        tree[ledid+12].on()
        time.sleep(.2)
        tree[ledid].off()
        tree[ledid+12].off()
pause()
