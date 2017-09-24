from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard(pwm=True)

sb.on()  # all leds on
sleep(1)
sb.off()  # all leds off
sleep(1)
for strip in sb:
    strip.lights.red.pulse()
    sleep(1)
    strip.lights.green.pulse()
    sleep(1)
