import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
    
def connect():
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect('NITESH_ANAND', 'jrnka@2019')
        while wlan.status() == 1:
            pass #wait while connecting

def isconnected():
    return wlan.isconnected();