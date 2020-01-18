# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
from datetime import datetime
from thaitts import TTS
import speech_recognition as sr2
from pyvadrun import run
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

def go2add():
    tts.listen("กรุณาพูดหัวข้อการบันทึกในครั้งนี้ค่ะ แล้วหยุดสัก 2 3 วินาทีนะคะ")
    run("d1.wav")
    with sr2.WavFile("d1.wav") as source:
        print("รับเสียง")
        title =  r.record(source)
        print(title)
    tts.listen("หลังจากนี้จะเป็นการบันทึกข้อความ ถ้าบันทึกเสร็จแล้วให้หยุดพูดสัก 2 ถึง 3 วินาทีนะคะ")
    run("d2.wav")
    with sr2.WavFile("d2.wav") as source:
        print("รับเสียง")
        note =  r.record(source)
        print(note)
    return add(title,note)


def check_word(text):
    if ("จด" in text or "บันทึก" in text) and ("อ่าน" not in text and "ค้น" not in text):
        go2add()
    else : print("ฉันไม่เข้าใจในสิ่งที่คุณพูด หรือ พูดใหม่อีกครั้ง ")


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