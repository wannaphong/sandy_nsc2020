# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
from datetime import datetime
from thaitts import TTS
import speech_recognition as sr2
from pyvadrun import run as _run
from pythainlp.util import thai_day2datetime, thai_time2time, thai_time
import pytz
db = TinyDB('./diary.json')
timezone = pytz.timezone('Asia/Bangkok')
tts = TTS()
r = sr2.Recognizer()

print("ฟังก์ชั่นบันทึกและอ่านไดอารี่")

def add(title:str,note:str)->None:
    """
    บันทึกไดอารี
    """
    global db,timezone
    t= timezone.localize(datetime.now())
    db.insert({'date': str(t),'title':title,'note':note})
    return "บันทึกเรียบร้อยแล้วค่ะ"
N = Query()

def search_audio():
    global _run
    tts.listen("กรุณาพูดข้อความที่ต้องการค้นหาค่ะ")
    _run("ds1.wav")
    with sr2.WavFile("ds1.wav") as source:
        print("รับเสียง")
        audio =  r.record(source)


def go2add():
    global _run
    tts.listen("กรุณาพูดหัวข้อการบันทึกในครั้งนี้ค่ะ แล้วหยุดสัก 2 3 วินาทีนะคะ")
    _run("d1.wav")
    with sr2.WavFile("d1.wav") as source:
        print("รับเสียง")
        audio =  r.record(source)
    title=r.recognize_google(audio,language = "th-TH")
    print(title)
    tts.listen("หลังจากนี้จะเป็นการบันทึกข้อความ ถ้าบันทึกเสร็จแล้วให้หยุดพูดสัก 2 ถึง 3 วินาทีนะคะ")
    _run("d2.wav")
    with sr2.WavFile("d2.wav") as source:
        print("รับเสียง")
        audio =  r.record(source)
    note=r.recognize_google(audio,language = "th-TH")
    print(note)
    return add(title,note)

def look(day:str="วันนี้"):
    global db,N,timezone
    d=str(timezone.localize(thai_day2datetime(day))).split()[0]
    text = ""
    s = db.search(N.date.search(d))#((N.date.search(d)) & (N.alert == True))
    #print(s)
    if len(s)==0:
        return "ไม่มีการบันทึก"+day+"ค่ะ"
    text += "รายการบันทึกความจำ"+day+"มีดังนี้"+"\n"
    j=1
    for i in s:
        t = i["date"].split()[1].replace("+07:00","").split('.')[0]
        text += "รายการที่ "+str(j)+" เวลา "+t+" หัวข้อ"+i["title"]+" มีการบันทึกว่า "+i["note"]+" ค่ะ\n"
        j+=1
    return text


def check_word(text:str):
    if ("จด" in text or "เขียน" in text) and "บันทึก" in text and "วันนี้" not in text:
        return go2add()
    elif ("ค้น" in text or "อ่าน" in text) and "วันนี้" in text:
        return look(day="วันนี้")
    return "ฉันไม่เข้าใจในสิ่งที่คุณพูด ให้พูดใหม่อีกครั้งค่ะ "


def read_diary():#อ่านไดอารี่ทั้งหมด 
    pass
"""    for i in result:
        print(i)

def  select_diary():   
    mycursor.execute("select * from  diary_data WHERE date_diary='2019-12-06'")
    select = mycursor.fetchall() #fetch data 
    for s in select:
        print(s)

def insert_daiary(): 

    mycursor = mydb.cursor()
    sql = "INSERT INTO diary_data (toppic, detail_diary,date_diary) VALUES (%s,%s,%s)"
    value = ("ไปต่างจังหวัดกับครอบครัว","วันนี้เราได้ไปเที่ยวต่างจังหวัดกับครอบครัว ฉันมีความสุขมาก ","2019-12-10") 
    mycursor.execute(sql,value)
    mydb.commit()
    
#call function 
check_word("อ่านไดอารี่ทั้งหมด")
"""