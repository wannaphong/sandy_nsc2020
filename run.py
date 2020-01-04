# -*- coding: utf-8 -*-
import time
from gettime.nowtime import now
from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
from tts import TTS
from sos import sent
from vad import run
from news.news import gethotnews
from pythainlp.tokenize import word_tokenize
import sys
from pydub import AudioSegment
from pydub.playback import play
from weather.weather import now as now_w
from music.song import music
from threading import Event
m = music()
def playsound(path):
    song = AudioSegment.from_file(path)
    play(song)
print('start')
t=TTS()
r = sr.Recognizer()
#t.listen("NSC 2020 แสนดีผู้ช่วยผู้สูงอายุ กำลังเริ่มต้นการทำงาน")
def on_prediction(prob:float)->None:
    print(print(prob) if prob > 0.5 else '.', end='', flush=True)

stauts=""
'''
def process(text:str)->str:
    global m
    if "เวลา" in text:
        text=now()
    elif "ออก" in text or "ลาก่อน" in text:
        text="ลาก่อนค่ะ"
    elif "ช่วยเหลือ" in text or "ฉุกเฉิน" in text:
        text="กำลังขอความช่วยเหลือผ่านไลน์ค่ะ"
        sent()
    elif "ข่าว" in text:
        text=gethotnews()
    elif ("สภาพอากาศ" in text or "อากาศ" in text) and ("ตอนนี้" in text or "วันนี้" in text):
        text=now_w().replace('\n','')
    elif "ฟัง" in text and 'ต่อ' in text:
        m.play()
        text=""
    elif 'เปิด' in text and 'เพลง' in text:
        text=text.split('เพลง')[1]
        m.change(text)
        #text=text
    elif 'ปิด' in text and ('เพลง' in text or 'เสียง' in text):
        text="ปิดเรียบร้อยแล้วค่ะ"
        m.stop()
    else:
        text="คุณพูดว่า "+text
    return text
'''
from pythainlu.intent_classification.MultinomialNB import nb
from weather.weather import text2com as wcom
from news.news import text2com as ncom
import dill
with open('modelclass2.model', 'rb') as in_strm:
    clf = dill.load(in_strm)[0]
def process(text:str)->str:
    global clf,nb,wcom,ncom
    tag=str(clf.predict([text])[0])
    print(tag)
    if clf.predict_proba([text]).max()<0.3:
        text = "ระบบยังไม่รองรับคำสั่งนี้"
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
    elif tag == "sos":
        text = "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ"
        sent()
    else:
        text = "ระบบยังไม่รองรับ"
    return text

def sound(text):
    global t
    if text == "ค่ะ":
        playsound('./sound/ค่ะ.mp3')
    elif text == "ลาก่อนค่ะ":
        playsound('./sound/bye.mp3')
    elif text=='':
        pass
    else:
        t.listen(text)
def on_activation():
    global stauts
    global m
    m.pause()
    sound("ค่ะ")
    global r
    print("hotword detected")
    run()
    with sr.WavFile("recording.wav") as source:
        print("รับเสียง")
        audio =  r.record(source) #r.listen(source)
    print("กำลังประมวลผล")
    try:
        print("กำลังรอเสียง")
        text=r.recognize_google(audio,language = "th-TH")
        print(text)
        tt=process(text)
        sound(tt)
        if tt=="ลาก่อนค่ะ":
            stauts="exit"#sys.exit(0)
    except sr.RequestError as e:
        print(e)
    except Exception as e:
        print(e)

engine = PreciseEngine('C:\\Users\\TC\\Anaconda3\\Scripts\\precise-engine.exe', 'jao-sandy.pb') 
# PreciseEngine(ที่ตั้งโฟลเดอร์ Scripts ของ precise-engine ,  ไฟล์ model)
# หากรันบน Linux ใช้ precise-engine/precise-engine ใน precise-engine
runner = PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation, sensitivity=0.6, trigger_level=3)
runner.start()
"""while 1:
    time.sleep(100)
    if stauts=="exit":
        break"""
Event().wait()