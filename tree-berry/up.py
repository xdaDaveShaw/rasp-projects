from gpiozero import LEDBoard
from signal import pause
import time

star = LEDBoard(2, pwm=True)
first = LEDBoard(17, 16, 11, 19, 25, 27, pwm=True)
second  = LEDBoard(4, 9, 13, 18, 5, 8, 26, pwm=True)
third = LEDBoard(22, 24, 20, 12, 6, 15, pwm=True)
bottom = LEDBoard(14, 10, 23, 21, 7, pwm=True)

star.off()
first.off()
second.off()
third.off()
bottom.off()

duration = 0.3

for counter in range(1000):
    bottom.on()
    time.sleep(duration)
    third.on()
    time.sleep(duration)
    second.on()
    time.sleep(duration)
    first.on()
    time.sleep(duration)
    star.on()
    time.sleep(duration)
    star.off()
    time.sleep(duration)
    first.off()
    time.sleep(duration)
    second.off()
    time.sleep(duration)
    third.off()
    time.sleep(duration)
    bottom.off()
    time.sleep(duration)
pause()
