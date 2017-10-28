from gpiozero import StatusBoard
from time import sleep

sb = StatusBoard(pwm=True)

#DAS: Doesn't quite stop right yet
keepGoing = 1
def stop():
    keepGoing = 0
    
sb.five.button.when_pressed = stop

while keepGoing == 1:
    sb.on()  # all leds on
    sleep(1)
    sb.off()  # all leds off
    sleep(1)
    sb.one.button.wait_for_press()
    for strip in sb:
        strip.lights.red.pulse()
        sleep(1)
        strip.lights.green.pulse()
        sleep(1)
    sb.four.button.wait_for_press()
    sb.off()
    
