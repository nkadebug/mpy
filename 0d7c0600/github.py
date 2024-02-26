from requests import get
from json import dumps
from machine import unique_id
from ubinascii import hexlify

def getPath(path):
    print('get : ',path)
    res = get("https://api.github.com/repos/nkadebug/mpy/contents/"+path,headers={"User-Agent":"MPY Device"})
    try:
        for item in res.json():
            if item['type']=='file':
                print(item['path'])
            else:
                getPath(item['path'])
    except:
        print(res.text)

did = hexlify(unique_id()).decode('utf-8')
getPath(did)