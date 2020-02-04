# -*- coding: utf-8 -*-
from gtts import gTTS
text = input("ข้อความของคุณ : ")
tts = gTTS(text='สวัสดีฉัน ฉันกำลังพูดภาษาไทยค่ะ',lang='th') # text คือ ข้อความ lang คือ รหัสภาษา
name = input("ชื่อไฟล์ : ")
tts.save(name+'.mp3')
print("ข้อความ : "+text+"\n\nไฟล์ "+name+".mp3")