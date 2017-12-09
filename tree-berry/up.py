from gpiozero import LEDBoard
from signal import pause
import time

#GPIO | Tree
#2  star
#3  
#4  1
#5  7
#6  16
#7  22
#8  6
#9  14
#10 8
#11 21
#12 15
#13 3
#14 19
#15 2
#16 9
#17 10
#18 20
#19 18
#20 17
#21 4
#22 24
#23 23
#24 13
#25 5
#26 12
#27 11

star = LEDBoard(2, pwm=True)
fourth = LEDBoard(17, 16, 11, 19, 25, 27, pwm=True)
third  = LEDBoard(4, 9, 13, 18, 5, 8, 26, pwm=True)
second = LEDBoard(22, 24, 20, 12, 6, 15, pwm=True)
bottom = LEDBoard(14, 10, 23, 21, 7, pwm=True)

star.off()
fourth.off()
third.off()
second.off()
bottom.off()

duration = 0.3

for counter in range(1000):
    bottom.on()
    time.sleep(duration)
    second.on()
    time.sleep(duration)
    third.on()
    time.sleep(duration)
    fourth.on()
    time.sleep(duration)
    star.on()
    time.sleep(duration)
    star.off()
    time.sleep(duration)
    fourth.off()
    time.sleep(duration)
    third.off()
    time.sleep(duration)
    second.off()
    time.sleep(duration)
    bottom.off()
    time.sleep(duration)
pause()
