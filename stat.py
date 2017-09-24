from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard(pwm=True)

sb.on()  # all leds on
sleep(1)
sb.off()  # all leds off
sleep(1)
sb.one.lights.green.value = 0.5  # green led of first strip at half brightness
sleep(1)
#sb.two.value = (0.5, 0.5)  # both leds of second strip at half brightness
sleep(1)
sb.one.lights.pulse()  # both leds of first strip fading in and out
sleep(1)
sb.two.lights.pulse()  # both leds of second strip pulsing in opposite timing with the first
