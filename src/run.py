# -*- coding: utf-8 -*-
"""
แสนดี : คู่บ้านผู้สูงอายุ
"""
import sys
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=UserWarning)
from music.song import song,tum,m#,s
import os
def get_path(p):
    return os.path.join(os.path.dirname(__file__),p)
m.play_other(get_path('./sound/on.mp4'))
m.play()
# python พื้นฐาน
import time
from threading import Event, Thread
import dill
print("1 : import hotword")
# Hotword
from precise_runner import PreciseEngine, PreciseRunner
engine = PreciseEngine('precise-engine', get_path('jao-sandy.pb'))
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
#from pygame import mixer
#mixer.init()
#
print("import ฟังก์ชัน")
from weather.weather import now as now_w

from general import general
from weather.weather import text2com as wcom
from news.news import text2com as ncom
from alert import text2com as acom
from alert.run import alert_run
from iot import text2com as iotcom
from diary import check_word as diarycom
print("5 : nlu")
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
with open(get_path('modelclass2.model'), 'rb') as in_strm:
    clf = dill.load(in_strm)
t=TTS()
m.stop()
m.play_other(get_path("./sound/open.mp4"))
m.play()
print("6 : ASR")
r = sr.Recognizer()
print(7)
#t.listen("NSC 2020 แสนดีผู้ช่วยผู้สูงอายุ กำลังเริ่มต้นการทำงาน")
def on_prediction(prob:float)->None:
    print(print(prob) if prob > 0.5 else '.', end='', flush=True)

print(8)

def process(text:str)->tuple:
    global clf,wcom,ncom,acom,song,tum,n,sound,iotcom,m
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
        text = now(text)
    elif tag == "alert":
        text = acom(text)#"ระบบการแจ้งเตือน ยังไม่พร้อมใช้งาน"
    elif tag == "fan" or tag == "light":
        text = iotcom(text,tag)
    elif tag == "music":
        if 'เปิด' in text:
            sound("กำลังเปิดเพลงอยู่ กรุณารอสักครู่ค่ะ")
        text = song(text)#"ระบบฟังเพลง"
        if 'เล่นเพลงต่อ' in text:
            m.play_old()
    elif tag == "religion":
        if 'เปิด' in text:
            sound("กำลังเปิดธรรมะอยู่ กรุณารอสักครู่ค่ะ")
        text = tum(text)#"ระบบฟังธรรมะ"
    elif tag == "weather":
        text = wcom(text)
    elif tag == "news":
        text = ncom(text)
        sound("กำลังหาข่าวอยู่ กรุณารอสักครู่ค่ะ")
    elif tag == "sos":
        text = sent()
    else:
        text = "ระบบยังไม่รองรับ"
    print("ข้อความจากฟังก์ชัน : "+str(text))
    return (text,tag)
soundfile={
    "ค่ะ":'./sound/ค่ะ.mp3',
    "ลาก่อนค่ะ":'./sound/bye.mp3',
    "กำลังหาข่าวอยู่ กรุณารอสักครู่ค่ะ":'./sound/news1.mp3',
    "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ":'./sound/sos1.mp3',
    "ระบบยังไม่รองรับฟังก์ชันนี้ค่ะ":'./sound/notsup.mp3',
    "nointernet":'./sound/notnet.mp3',
    "ระบบไอโอทีไม่รองรับการทำงานนี้ค่ะ":'./sound/iot-not.mp3',
    "เปิดไฟแล้วค่ะ":'./sound/l-on.mp3',
    "ปิดไฟแล้วค่ะ":'./sound/l-off.mp3',
    "เปิดพัดลมแล้วค่ะ":'./sound/f-on.mp3',
    "ปิดพัดลมแล้วค่ะ":'./sound/f-off.mp3',
    "คุณยังไม่สั่งเปิดเพลงค่ะ":'./sound/m-not.mp3',
    "เล่นเพลงต่อแล้วค่ะ":'./sound/m-con.mp3',
    "ปิดเพลงเรียบร้อยแล้วค่ะ":'./sound/m-close.mp3',
    "หยุดเพลงเรียบร้อยแล้วค่ะหากต้องการฟังต่อให้สั่งฟังเพลงต่อได้เลยนะคะ":'./sound/m-s.mp3',
    "เล่นเพลงถัดไปแล้วค่ะ":'./sound/m-con2.mp3',
    "คุณยังไม่สั่งเปิดธรรมะค่ะ":'./sound/t-not.mp3',
    "เล่นธรรมะต่อแล้วค่ะ":"./sound/t-con.mp3",
    "ปิดธรรมะเรียบร้อยแล้วค่ะ":"./sound/t-close.mp3",
    "หยุดธรรมะเรียบร้อยแล้วค่ะหากต้องการฟังธรรมะต่อให้สั่งฟังธรรมะต่อได้เลยนะคะ":"./sound/t-con2.mp3",
    "เล่นธรรมะถัดไปแล้วค่ะ":"./sound/t-next.mp3"
}

def sound(text):
    global t
    for i in soundfile.keys():
        if text == i:
            playsound(get_path(soundfile[i]))
            return None
    if text == "":
        pass
    else:
        t.listen(text)
    return None
print(9)
#instance = vlc.Instance()
#on_news = False
#สร้าง MediaPlayer พร้อม instance พื้นฐาน
print(10)
#_player = instance.media_player_new()
on_run =False
on_news=False
def on_activation():
    global t,on_news,v
    global m,on_run,_player#instance,on_news
    m.pause()
    if is_internet()==False:
        sound("nointernet")
        return ''
    if on_news==True:
        #mixer.music.stop()
        m.stop()
        on_news=False
    sound("ค่ะ")
    global r
    print("hotword detected")
    run()
    with sr.WavFile("recording.wav") as source:
        print("รับเสียง")
        audio =  r.record(source) #r.listen(source)
    print("กำลังประมวลผล")
    m.play_other(get_path('./sound/361217__littlejest__waiting.mp3'))
    m.play()
    try:
        print("กำลังรอเสียง")
        text=r.recognize_google(audio,language = "th-TH")
        print(text)
        tt=process(text)
        m.stop()
        print(tt)
        if tt[1] == 'news':
            on_news=True
            #mixer.music.load('./news.mp3')
            print("ok news")
            #mixer.music.play()
            #m.stop()
            m.play_other('./news.mp3')
            m.play()
            #playsound('./news.mp3')
        else:
            #m.stop()
            sound(tt[0])
        
    except sr.RequestError as e:
        m.stop()
        print(e)
    except Exception as e:
        m.stop()
        print(e)
    finally:
        on_run=False

print(11)
def main():
    runner = PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation, sensitivity=0.5, trigger_level=3)
    print(12)
    runner.start()
    print(13)
    thread1 = Thread(target = alert_run)
    thread1.start()
    thread1.join()
    #runner.start()
    m.stop()
    Event().wait()
if __name__=='__main__':
   main()