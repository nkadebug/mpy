from time import ticks_ms,sleep_ms
from machine import Pin

led = Pin(2,Pin.OUT)
ticks = 0

while True:
    if ticks_ms() > ticks + 1000:
        ticks = ticks_ms()
        led.off()
        sleep_ms(10)
        led.on()
        