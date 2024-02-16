from machine import Pin
from dht import DHT11
import json

s = DHT11(Pin(2))

def read():
    s.measure();
    return json.dumps({'humi':s.humidity(),'temp':s.temperature(),"_ts":{".sv":"timestamp"}});