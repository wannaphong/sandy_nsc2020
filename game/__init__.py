from .vad import run
from .tts import TTS
import speech_recognition as sr2

t = TTS()
r = sr2.Recognizer()

data=[
    ("อะไรเอ่ย หัวเป็นหนามถามไม่พูด", "พระพุทธรูป",""),
    ("อะไรเอ่ยสี่ตีนเดินมาหลังคามุงกระเบื้อง", "เต่า",""),
    ("อะไรเอ่ยชื่อเหมือนคนตายมีปีกบินได้ หากินกับดอกไม้", "ผีเสื้อ",""),
    ("นกอะไรไม่ใช่ของเรา", "นกเขา",""),
    ("มัจฉาหนึ่งถูกขังไม่ดิ้นรน", "ปลากระป๋อง",""),
    ("อะไรเอ่ยต้นเท่าครก ใบปรกดิน", "ตะไคร้",""),
    ("อะไรเอ่ยสุกไม่หอม งอมไม่หล่น แห้งคาต้น คนกินได้", "ข้าวโพด","เพราะเมื่อแก่ได้ที่ก็ไม่หอมแห้งอยู่กับต้น"),
    ("สัตว์อะไรอยู่ในน้ำ คนชอบเรียกผิด", "วาฬ","เพราะคนชอบเรียกว่าปลาวาฬ"),
    ("อะไรเอ่ยต้นเท่าเข็มใบเต็มทุ่งนา","ผักแว่น","เป็นผักที่มีลำต้นเล็กขนาดต้นถั่วงอก ใบเป็นรูปหัวใจ 3 แฉกติดกัน เป็นรูปกลม มัก"),
    ("อะไรเอ่ยตัวอยู่นา ตาอยู่บ้าน อยู่นากัดข้าว อยู่บ้านกัดฝา","ตะปู",""),
    ("อะไรเอ่ย มีหาง มีปาก มีตา กินปลาเป็นอาหาร","แห",""),
    ("อะไรเอ่ยกลางวันเก็บใส่กระบาย กลางคืนกระจายออก","ดาว",""),
    ("อะไรเอ่ยเขียวชอุ่มพุ่มไสว ไม่มีใบมีแต่เม็ด","ฝน",""),
    ("อะไรเอ่ยไม่ใกล้ไม่ไกลมองเห็นรำไร", "จมูก",""),
    ("น้ำอะไรไม่เคยขึ้น","น้ำตก",""),
    ("กาไม่ใช่กาแท้  การ่อแร่เกาะกิ่งไม้","กาฝาก",""),
    ("อยู่ในน้ำเป็นปลา อยู่สุขศาลาเป็นคน","หมอ",""),
    ("โตเท่าภูเขา เบานิดเดียว","เมฆ",""),
    ("สุกเต็มต้น เก็บกินไม่ได้","แดด","เป็นแสงแดด"),
    ("ต้นสีบาทพาดข้างรั้ว","ผักตำลึง","")
]

def game():
    global t,r
    t.listen("เกมส์ปริศนาทายคำ\nหากคุณต้องการเลิกเล่น ให้พูดว่าเลิกเล่น\nถ้าคุณขอยอมแพ้ให้พูดว่าเฉลยหรือยอมแพ้")
    t.listen("สัตว์อะไรอยู่ในน้ำ คนชอบเรียกผิด")
    while True:
        run()
        with sr2.WavFile("recording.wav") as source:
            print("รับเสียง")
            audio =  r.record(source)
            print(audio)
        text=r.recognize_google(audio,language = "th-TH")
        if 'วาฬ' in text:
            t.listen("ถูกต้องแล้วค่ะ\nข้อต่อไปกัน\n\n\nหากคุณต้องการเลิกเล่น ให้พูดว่าเลิกเล่น")
            break
        elif "เฉลย" in text or "ยอมแพ้" in text:
            t.listen("วาฬค่ะ")
            break
        elif "ทวน" in text:
            t.listen("สัตว์อะไรอยู่ในน้ำ คนชอบเรียกผิด")
        elif "เลิกเล่น" in text:
            t.listen("กำลังออกจากเกม")
            break
        else:
            t.listen('ยังไม่ถูกค่ะ')
    t.listen("จบเกมแล้วค่ะ")
        