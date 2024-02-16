from requests import put,post
from sensor import read
from json import dumps,loads
import btree

dbUrl="https://iotbug-default-rtdb.asia-southeast1.firebasedatabase.app"
apiKey="AIzaSyCdqJmPBvceTAGYtuRR6BsEE3l3rz018Qg"

email="nka.debug@gmail.com"
password="nka@1990"

sensorid="dht"

try:
    f = open("auth", "r+b")
except OSError:
    f = open("auth", "w+b")
db = btree.open(f)

def upload():
    
    user = loads(db.get('user',b"{}").decode('utf-8'))
    #print(user)
    
    if not user.get('idToken') or not user.get('localId'):
        login(email,password)
        return
    
    url = "{}/{}/{}.json?auth={}".format(dbUrl,user.get('localId'),sensorid,user.get('idToken'))
    #print(url)
    
    try:
        data = read()
        #print(data)
        
        try:
            res = put(url,data=data).json()
            #print(res)
            
            if res.get('error'):
                login(email,password)
            else:
                print("Uploaded",res)
                
        except:
            print("IOTBug Upload Error")
    except:
        print("Sensor Read Error")

def login(email,password):
    
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={}".format(apiKey)
    
    res = post(url,data=dumps({'email':email,'password':password,'returnSecureToken':True}))
    
    if res.json().get('error'):
        print(res.text)
        db[b'user'] = "{}"
        db.flush()
        
    else:
        print('Logged in as',email,"uid",res.json().get('localId'))
        db[b'user'] = res.text
        db.flush()