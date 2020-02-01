# -*- coding: utf-8 -*-
"""
แสนดี : คู่บ้านผู้สูงอายุ
"""
from pyvlc import quitfile
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=UserWarning)
# python พื้นฐาน
import time
import sys
from threading import Event, Thread
import dill
print("1 : import hotword")
# Hotword
from precise_runner import PreciseEngine, PreciseRunner
engine = PreciseEngine('precise-engine', 'jao-sandy.pb')
print("2 : import AER, TTS")
# AER, TTS
import speech_recognition as sr
from thaitts import TTS,playsound
print("3 : import ฟังก์ชัน")
# ฟังก์ชัน
from gettime.nowtime import now # ถามวันเวลา
from sos import sent
from pyvadrun import run
print("4 : import vlc")
#from news.news import gethotnews
import vlc
from pydub import AudioSegment
from pydub.playback import play
from weather.weather import now as now_w
from music.song import song,tum,m#,s
from general import general
#from nn import nb #pythainlu.intent_classification.
from weather.weather import text2com as wcom
from news.news import text2com as ncom
from alert import text2com as acom
from alert.run import alert_run
from iot import text2com as iotcom
from diary import check_word as diarycom
print("5 : nlu")
#from pynput.keyboard import Key, Listener
import urllib
from urllib.request import urlopen
def is_internet():
    """
    Query internet using python
    :return:
    """
    try:
        urlopen('https://sandy.numfa.com', timeout=1)
        return True
    except Exception as Error:
        print(Error)
        return False
#m = music()
stauts=""
with open('modelclass2.model', 'rb') as in_strm:
    clf = dill.load(in_strm)
t=TTS()
print("6 : ASR")
r = sr.Recognizer()
print(7)
#t.listen("NSC 2020 แสนดีผู้ช่วยผู้สูงอายุ กำลังเริ่มต้นการทำงาน")
def on_prediction(prob:float)->None:
    print(print(prob) if prob > 0.5 else '.', end='', flush=True)

print(8)

def process(text:str)->tuple:
    global clf,wcom,ncom,acom,song,tum,n,sound,iotcom
    tag=str(clf.predict([text])[0])
    print("ฟังก์ชัน : "+tag)
    _p = clf.predict_proba([text]).max()
    print("ความน่าจะเป็นของฟังก์ชัน : "+str(_p))
    g = general(text)
    if g[1]:
        text = g[0]
    elif ("บันทึก" in text or "ไดอารี่" in text) or "ไดอารี" in text:
        text = diarycom(text)
    elif _p<=0.6:
        text = "ระบบยังไม่รองรับฟังก์ชันนี้ค่ะ"
    elif "ออก" in text and "โปรแกรม" in text:
        text = "ลาก่อนค่ะ"
    elif text == "เจ้าแสนดี" or text == "แสนดี":
        text = "สวัสดีค่ะ"
    elif tag == "asktime":
        text=now(text)
    elif tag == "alert":
        text = acom(text)#"ระบบการแจ้งเตือน ยังไม่พร้อมใช้งาน"
    elif tag == "fan" or tag == "light":
        text = iotcom(text,tag)
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
        #text = "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ"
        text = sent()
    else:
        text = "ระบบยังไม่รองรับ"
    print("ข้อความจากฟังก์ชัน : "+text)
    return (text,tag)

def sound(text):
    global t
    if text == "ค่ะ":
        playsound('./sound/ค่ะ.mp3')
    elif text == "ลาก่อนค่ะ":
        playsound('./sound/bye.mp3')
    elif text == "กำลังหาข่าวอยู่ กรุณารอสักครู่ค่ะ":
        playsound('./sound/news1.mp3')
    elif text == "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ":
        playsound('./sound/sos1.mp3')
    elif text == "ระบบยังไม่รองรับฟังก์ชันนี้ค่ะ":
        playsound('./sound/notsup.mp3')
    elif text == "nointernet":
        playsound('./sound/notnet.mp3')
    elif text == "":
        pass
    else:
        t.listen(text)
print(9)
#instance = vlc.Instance()
#on_news = False
#สร้าง MediaPlayer พร้อม instance พื้นฐาน
print(10)
#_player = instance.media_player_new()
on_run =False
on_news=False
def on_activation():
    global t,on_news
    global m,on_run,_player#instance,on_news
    m.pause()
    #s.pause()
    #if on_news:
    #    _player.stop()
    if is_internet()==False:
        sound("nointernet")
        return ''
    if on_news==True:
        quitfile()
        on_news=False
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
        if tt[1] == 'news':
            on_news=True
        else:
            sound(tt[0])
        #if tt[1] == 'news' and "ขออภัยค่ะ" not in tt[0]:
        #    t.gTTS1(tt[0],'news.mp3')
        #    media = instance.media_new('news.mp3')
        #    _player.set_media(media)
        #    _player.play()
        #    on_news=True
        #elif tt=="ลาก่อนค่ะ":
        #    sys.exit(0)
        #else:
        #    sound(tt[0])
        
    except sr.RequestError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        on_run=False

print(11)
runner = PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation, sensitivity=0.5, trigger_level=3)
print(12)
runner.start()
print(13)
thread1 = Thread(target = alert_run)
thread1.start()
thread1.join()
#runner.start()

Event().wait()
