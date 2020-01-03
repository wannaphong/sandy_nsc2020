# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from pythainlu.intent_classification.MultinomialNB import nb
from weather.weather import text2com as wcom
from gettime.nowtime import now
from news.news import text2com as ncom
import dill
with open('modelclass2.model', 'rb') as in_strm:
    clf = dill.load(in_strm)[0]
#clf =  joblib.load('modelclass.model')
def process(text:str)->str:
    global clf,nb,wcom,ncom
    tag=str(clf.predict([text])[0])
    print(tag)
    print(clf.predict_proba([text]).max())
    #print(list(tag))
    if clf.predict_proba([text]).max()<0.3:
        text = "ระบบยังไม่รองรับข้อความนี้"
    elif tag == "asktime":
        text=now()
    elif tag == "alert":
        text = "ระบบการแจ้งเตือน ยังไม่พร้อมใช้งาน"
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
    else:
        text = "ระบบยังไม่รองรับ"
    return text

while True:
    t =  input("text : ")
    if t =="exit":
        break
    print(process(t))
    print()