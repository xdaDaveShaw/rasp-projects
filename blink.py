# From: http://www.instructables.com/id/Your-First-Project-in-Raspberry-Pi-LED-Blinking/?ALLSTEPS
# License: https://creativecommons.org/licenses/by-nc-sa/2.5/
# Changes: No

import RPi.GPIO as Blink_led
import time
Blink_led.setmode(Blink_led.BOARD)
Blink_led.setup(3, Blink_led.OUT)
for counter in range(0,10000):
    Blink_led.output(3,True)
    time.sleep(1)
    Blink_led.output(3,False)
    time.sleep(1)
Blink_led.output(False)
