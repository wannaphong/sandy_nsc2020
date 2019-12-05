import time
from gettime.nowtime import now
from precise_runner import PreciseEngine, PreciseRunner
import speech_recognition as sr
from tts import TTS
from vad import run
import sys
print('start')
t=TTS()
r = sr.Recognizer()
t.listen("NSC 2020 แสนดีผู้ช่วยผู้สูงอายุ กำลังเริ่มต้นการทำงาน")
def on_prediction(prob:float)->None:
    print(print(prob) if prob > 0.5 else '.', end='', flush=True)

"""def on_activation():
    print('Activation')
    winsound.PlaySound("*", winsound.MB_OK)"""
stauts=""
def process(text:str)->str:
    if "เวลา" in text:
        text=now()
    elif "ออก" in text or "ลาก่อน" in text:
        text="ลาก่อนค่ะ"
    else:
        text="คุณพูดว่า "+text
    return text
def on_activation():
    global stauts
    global t
    t.listen("ค่ะเจ้านาย")
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
        t.listen(tt)
        if tt=="ลาก่อนค่ะ":
            stauts="exit"#sys.exit(0)
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
    if stauts=="exit":
        break