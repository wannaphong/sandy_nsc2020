# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
from pythainlp.util import thai_day2datetime, thai_time2time, thai_time
from pythainlp.util import thai_strftime
import pytz
import datetime as dt
import pytz
from pythainlp.tag.named_entity import ThaiNameTagger
from nltk.tokenize import RegexpTokenizer
pattern = r'\<(.*?)\>(.*?)\<\/(.*?)\>'
tokenizer = RegexpTokenizer(pattern)
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

"""
รับวันในสัปดาห์
>>> import datetime
>>> datetime.datetime.today()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
>>> datetime.datetime.today().weekday()
4
from pythainlp.util import thai_strftime
>>> thai_strftime(datetime.datetime.today(), "%A")
'วันอังคาร'
"""
def find_day(date):
    return thai_strftime(date, "%A")

N = Query()
def look(day="วันนี้"):
    global db,N,timezone
    d=str(timezone.localize(thai_day2datetime(day))).split()[0]
    text = ""
    s = db.search(N.date.search(d))
    #print(s)
    if len(s)==0:
        return "ไม่มีการแจ้งเตือน"+day+"ค่ะ"
    text += "รายการแจ้งเตือน"+day+"มีดังนี้"+"\n"
    j=1
    for i in s:
        t = i["date"].split()[1].replace("+07:00","")
        text += "รายการที่ "+str(j)+" เวลา "+t+" มีการแจ้งเตือนว่า "+i["text"]+" ค่ะ\n"
        j+=1
    return text


def text2com(text):
    global ner,tokenizer,thai_day2datetime,thai_time2time,add
    tag_ner = ner.get_ner(text,pos=False,tag=True)
    tt = tokenizer.tokenize(tag_ner)
    print(tt)
    d = None
    t = None
    for i in tt:
        temp_tag=i[0]
        temp_txt=i[1]
        if temp_tag == 'DATE':
            try:
                thai_day2datetime(temp_txt)
                d = temp_txt
            except:
                pass
        elif temp_tag == 'TIME':
            try:
                temp_txt = temp_txt.replace(" น.","").replace("น.","").replace(" น","")
                if ':' in temp_txt:
                    t = temp_txt
                else:
                    t =  thai_time2time(temp_txt)
            except:
                pass
    alert = None
    for i in ["แจ้งเตือนว่า","เตือนว่า","แจ้งว่า","แจ้งเตือน","เตือน","แจ้ง"]:
        if i in text:
            #print(text.split(i)[1])
            alert = text.split(i)[1]
            #print(alert)
            #break
    print(alert)
    if d == None and (alert != None and alert != '') and (t!=None and t!=''):
        d="วันนี้"
    
    if alert == None and alert == '':
        # ดูการแจ้งเตือนทั้งหมด
        # ยกเลิกการแจ้งเตือน
        text = 'ระบบแจ้งเตือนไม่รองรับคำสั่งของคุณ\nกรุณาลองคำสั่งอื่นนะคะ'
    elif (d!=None and d!='') and (t!=None and t!=''):
        add(d,t,alert)
        text = "เพิ่มการแจ้งเตือน "+d+" เวลา "+t+" มีการแจ้งเตือนว่า"+alert+" เรียบร้อยแล้วค่ะ"
    elif (t!=None and t!=''):
        add('วันนี้',t,alert)
        text = "เพิ่มการแจ้งเตือน "+d+" เวลา "+t+" มีการแจ้งเตือนว่า"+alert+" เรียบร้อยแล้วค่ะ"
    elif "แจ้งเตือน" in text or "เตือน" in text and (d!=None and d!=''):
        try:
            text = look(d)
        except:
            text = "ระบบยังไม่รองรับคำสั่งนี้"
    else:
        text = 'ระบบแจ้งเตือนไม่รองรับคำสั่งของคุณ\nกรุณาลองคำสั่งอื่นนะคะ'
    return text
"""
if __name__ == "__main__":
    date = input("วัน : ")
    t = input("เวลา (1:10) :")
    text = input("ข้อความ : ")
    add(date, t, text)
    print("เพิ่มเรียบร้อย\n\n")
    print()
"""