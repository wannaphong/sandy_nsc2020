# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
from pythainlp.util import thai_day2datetime, thai_time2time
import pytz
import datetime as dt
import pytz
from pythainlp.tag.named_entity import ThaiNameTagger
ner = ThaiNameTagger()
db = TinyDB('./db.json')
timezone = pytz.timezone('Asia/Bangkok')
def add(date:str,time:str,text:str)->None:
    global db,timezone
    t= time.split(":")
    hour = int(t[0])
    minute = int(t[1])
    d = timezone.localize(thai_day2datetime(date)).replace(hour=hour, minute=minute, second=0, microsecond=0)
    if d == None: pass
    db.insert({'date': str(d),'text':text})
    print(d)

def text2com(text):
    global ner
    print(ner.get_ner(text,pos=False,tag=True))
    return text

if __name__ == "__main__":
    date = input("วัน : ")
    t = input("เวลา (1:10) :")
    text = input("ข้อความ : ")
    add(date, t, text)
    print("เพิ่มเรียบร้อย\n\n")
    print()