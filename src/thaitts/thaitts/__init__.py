# -*- coding: utf-8 -*-
"""
ใช้สำหรับแปลงข้อความเป็นเสียง
"""
import requests
from gtts import gTTS
from pythainlp.tokenize import word_tokenize
from pythainlp.util import normalize
from pydub import AudioSegment
from pydub.playback import play
from .ai4thai import ai4thai
def playsound(path):
    song = AudioSegment.from_file(path)
    play(song)

def thaitts(text,url,filename):
    r = requests.get(url+text, allow_redirects=True)
    if r.status_code==200:
        file=open(filename, 'wb')
        file.write(r.content)
        file.close()
        r.close()
        return None
    else:
        r.close()
        raise RuntimeError("ไม่สามารถรันได้")


class TTS(object):
    def __init__(self,engine="g"):
        self.engine=engine
        self.thaitts="http://127.0.0.1:5000/tts?text="
    def gTTS1(self,text,filename):
        tts = gTTS(text=text,lang="th")
        tts.save(filename)
    def listen(self,text,play=True):
        text=normalize(text)
        if play and self.engine=="thaitts":
            self.list=word_tokenize(text)
            try:
                thaitts(" ".join(self.list),self.thaitts,"./t.wav")
                playsound('./t.wav')
            except:
                print("ไม่สามารถพูดได้ : "+str(text))
        elif play and self.engine=="g":
            self.gTTS1(text,"t.mp3")
            playsound('t.mp3')
        elif play and self.engine == "ai4thai":
            ai4thai(text,"t.mp3")
            playsound('t.mp3')

