from .vad import run
from .tts import TTS
import speech_recognition as sr2

t = TTS()
r = sr2.Recognizer()
def game():
    global t,r
    t.listen("เกมส์ทายคำ")
    t.listen("สัตว์อะไรอยู่ในน้ำ คนชอบเรียกผิด")
    while True:
        run()
        with sr2.WavFile("recording.wav") as source:
            print("รับเสียง")
            audio =  r.record(source)
            print(audio)
        text=r.recognize_google(audio,language = "th-TH")
        if 'วาฬ' in text:
            t.listen("ถูกต้องแล้วค่ะ")
            break
        elif "เฉลย" in text:
            t.listen("วาฬค่ะ")
            break
        elif "ทวน" in text:
            t.listen("สัตว์อะไรอยู่ในน้ำ คนชอบเรียกผิด")
        else:
            t.listen('ยังไม่ถูกค่ะ')
    t.listen("จบเกมแล้วค่ะ")
        