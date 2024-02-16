import time
import wifi
import iotbug

ticks = 0

while True:
    if time.ticks_ms() > ticks + 3000 :
        if wifi.isconnected():
            iotbug.upload();
        else:
            wifi.connect()
        ticks = time.ticks_ms();