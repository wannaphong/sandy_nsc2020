# -*- coding: utf-8 -*-
import time
from gettime.nowtime import now
from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
from tts import TTS
from sos import sent
from vad import run
from news.news import gethotnews
import sys
from pydub import AudioSegment
from pydub.playback import play
from weather.weather import now as now_w
from music.song import music
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

"""def on_activation():
    print('Activation')
    winsound.PlaySound("*", winsound.MB_OK)"""
stauts=""
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
    elif "อากาศ" in text and ("ตอนนี้" in text or "วันนี้" in text):
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
while 1:
    time.sleep(1)
    if stauts=="exit":
        break