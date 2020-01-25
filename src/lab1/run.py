# -*- coding: utf-8 -*-
import time
import winsound
from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
from tts import TTS
from vad import run
print('start')
t=TTS()
r = sr.Recognizer()
def on_prediction(prob):
    print(print(prob) if prob > 0.5 else '.', end='', flush=True)

"""def on_activation():
    print('Activation')
    winsound.PlaySound("*", winsound.MB_OK)"""

def on_activation():
    global t
    t.listen("หวัดดีค่ะ")
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
        t.listen("คุณพูดว่า "+text)
    except sr.RequestError as e:
        print(e)
    except Exception as e:
        print(e)

engine = PreciseEngine('C:\\Users\\TC\\Anaconda3\\Scripts\\precise-engine.exe', 'jao-sandy.pb') 
# PreciseEngine(ที่ตั้งโฟลเดอร์ Scripts ของ precise-engine ,  ไฟล์ model)
# หากรันบน Linux ใช้ precise-engine/precise-engine ใน precise-engine
runner = PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation, trigger_level=0)
runner.start()

while 1:
    time.sleep(1)