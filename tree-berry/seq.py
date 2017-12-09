from gpiozero import LEDBoard
import time

tree = LEDBoard(*range(2,28),pwm=True)

for counter in range(10000):
    for led in tree:
        print(led)
        led.on()
        time.sleep(10)
        led.off()
pause()
