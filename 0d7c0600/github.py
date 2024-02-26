from requests import get
from json import dumps
from machine import unique_id
from ubinascii import hexlify,a2b_base64

api = "https://api.github.com/repos/nkadebug/mpy/contents/"
headers = {"User-Agent":"MPY Device"}
did = hexlify(unique_id()).decode('utf-8')

def getPath(path):
    res = get(api+path,headers=headers)
    try:
        folder = res.json()
    except:
        print(res.text)
        
    for item in folder:
        if item['type']=='file':
            res = get(api+item['path'],headers=headers)
            
            try:
                file = res.json()
            except:
                print(res.text)
            
            try:
                name = item['path'].split(did+"/")[1]
                print('writing file :',name)
                f = open(name,'w')
                f.write(a2b_base64(file['content']))
                f.close()
            except:
                print('file write error')
        else:
            print('creating folder :',item['name'])
            import os
            os.mkdir(item['name'])
            getPath(item['path'])

getPath(did)