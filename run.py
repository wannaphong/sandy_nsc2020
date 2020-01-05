# -*- coding: utf-8 -*-
import time
from gettime.nowtime import now
from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
from tts import TTS,gTTS1
from sos import sent
from vad import run
from news.news import gethotnews
import vlc
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
from alert import text2com as acom
from music.song import song,tum,m,s
import dill
with open('modelclass2.model', 'rb') as in_strm:
    clf = dill.load(in_strm)[0]

from general import general

def process(text:str)->tuple:
    global clf,nb,wcom,ncom,acom,song,tum,n,sound
    tag=str(clf.predict([text])[0])
    print(tag)
    print(clf.predict_proba([text]).max())
    g = general(text)
    if g[1]:
        text = g[0]
    elif clf.predict_proba([text]).max()<0.3:
        text = "ระบบยังไม่รองรับคำสั่งนี้"
    elif tag == "asktime":
        text=now(text)
    elif tag == "alert":
        text = acom(text)#"ระบบการแจ้งเตือน ยังไม่พร้อมใช้งาน"
    elif tag == "fan" or tag == "light":
        text = "ระบบ IoT ยังไม่พร้อมใช้งาน"
    elif tag == "music":
        text = song(text)#"ระบบฟังเพลง"
    elif tag == "religion":
        text = tum(text)#"ระบบฟังธรรมะ"
    elif tag == "weather":
        text = wcom(text)
    elif tag == "news":
        text = ncom(text)
        sound("กำลังหาข่าวอยู่ กรุณารอสักครู่ค่ะ")
    elif tag == "sos":
        text = "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ"
        sent()
    else:
        text = "ระบบยังไม่รองรับ"
    print(text)
    return (text,tag)

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

instance = vlc.Instance()
on_news = False
#สร้าง MediaPlayer พร้อม instance พื้นฐาน
player = instance.media_player_new()
def on_activation():
    global stauts
    global m,s,player,on_news
    m.pause()
    s.pause()
    if on_news:
        player.stop()
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
        if tt[1] == 'news' and "ขออภัยค่ะ" not in tt[0]:
            gTTS1(tt[0],'news.mp3')
            media = instance.media_new('news.mp3')
            player.set_media(media)
            player.play()
            on_news=True
        else:
            sound(tt[0])
        if tt=="ลาก่อนค่ะ":
            stauts="exit"#sys.exit(0)
    except sr.RequestError as e:
        print(e)
    except Exception as e:
        print(e)

engine = PreciseEngine('precise-engine', 'jao-sandy.pb') #C:\\Users\\TC\\Anaconda3\\Scripts\\precise-engine.exe
# PreciseEngine(ที่ตั้งโฟลเดอร์ Scripts ของ precise-engine ,  ไฟล์ model)
# หากรันบน Linux ใช้ precise-engine/precise-engine ใน precise-engine
runner = PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation, sensitivity=0.5, trigger_level=4)
runner.start()
"""while 1:
    time.sleep(100)
    if stauts=="exit":
        break"""
Event().wait()