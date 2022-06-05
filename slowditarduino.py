import RPi.GPIO as GPIO
import time
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('cpd-team-slowdit-firebase-adminsdk-d8xli-a281bc9d78.json')
firebase_admin.initialize_app(cred,{
      'databaseURL': "https://cpd-team-slowdit-default-rtdb.asia-southeast1.firebasedatabase.app"
})

ref = db.reference('한남대 디자인팩토리')
ref.update({'count':"0"})
count = ref.get()
countli = list(count.values())
data = int(countli[0])


GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

while True:
    i = GPIO.input(18)
    if i == False:
        data+=1
        ref.update({'count':data})
        print("Motion Detected" + str(data))
        time.sleep(0.8)

GPIO.cleanup()
