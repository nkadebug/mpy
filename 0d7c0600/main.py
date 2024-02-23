from time import sleep_ms
from machine import Pin

led = Pin(2,Pin.OUT)

while True:
    print('Tick')
    led.on()
    sleep_ms(10)
    led.off()
    sleep_ms(3000)