# -*- coding: utf-8 -*-
#from sklearn.externals import joblib
from nn import nb
from weather.weather import text2com as wcom
from gettime.nowtime import now
from news.news import text2com as ncom
import dill
from sos import sent
from alert import text2com as acom
with open('modelclass2.model', 'rb') as in_strm:
    clf = dill.load(in_strm)
#clf =  joblib.load('modelclass.model')
def process(text:str)->tuple:
    global clf,nb,wcom,ncom,acom
    tag=str(clf.predict([text])[0])
    print(tag)
    if clf.predict_proba([text]).max()<0.3:
        text = "ระบบยังไม่รองรับคำสั่งนี้"
    elif tag == "asktime":
        text=now(text)
    elif tag == "alert":
        #text = "ระบบการแจ้งเตือน ยังไม่พร้อมใช้งาน"
        text = acom(text)
    elif tag == "fan" or tag == "light":
        text = "ระบบ IoT ยังไม่พร้อมใช้งาน"
    elif tag == "music":
        text = "ระบบฟังเพลง"
    elif tag == "religion":
        text = "ระบบฟังธรรมะ"
    elif tag == "weather":
        text = wcom(text)
    elif tag == "news":
        text = ncom(text)
    elif tag == "sos":
        text = "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ"
        sent()
    else:
        text = "ระบบยังไม่รองรับ"
    print(text)
    return (text,tag)

while True:
    t =  input("text : ")
    if t =="exit":
        break
    print(process(t))
    print()