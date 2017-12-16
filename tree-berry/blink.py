from gpiozero import LEDBoard
from signal import pause
import time

tree = LEDBoard(*range(2,28),pwm=True)
tree[0].blink()
for led in tree[1:]:
  led.blink()
  time.sleep(.2)
  
pause()
