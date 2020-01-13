import pafy
import vlc
from vlc import *
import urllib.request
import urllib.parse
import re
from tts import TTS
tt = TTS()

class music:
    def __init__(self):
        self.m="stop"
        self.status = True
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_list_player_new()
    def change(self,search):
        self.stop()
        self._search(search)
    def _search(self,search):
        self.query_string = urllib.parse.urlencode({"search_query" : search})
        self.html_content = urllib.request.urlopen("https://www.youtube.com/results?" + self.query_string)
        self.search_results = re.findall(r'href=\"\/watch\?v=(.{11})', self.html_content.read().decode())
        
        self.MediaList= self.Instance.media_list_new()
        for i in list((self.search_results)) :
            self.MediaList.add_media("https://www.youtube.com/watch?v=" + i)
        self.player.set_media_list(self.MediaList)
        self.play()

    
    def play(self):
        self.player.play()
        self.m = "play" 
    def stop(self):
        self.player.stop()
        self.m="stop"
    def pause(self):
        if self.m == 'play':
            self.player.pause()
            self.m="pause"
            print("status is pause!")

    def next(self):
        self.player.next()

m=music()
s=music()

def song(text:str)->str:
    global m
    
    if ("ฟัง" in text or "เล่น"in text) and 'เพลง'and 'ต่อ' in text: 
        text="เล่นเพลงต่อแล้วค่ะ"
        tt.listen(text)
        m.play()
        text=""
    elif 'เปิด' in text and 'เพลง' in text:
        text=text.split('เพลง')[1]
        m.change(text)
        #text=text
    elif 'ปิด' in text and ('เพลง' in text or 'เสียง' in text):
        text="ปิดเพลงเรียบร้อยแล้วค่ะ"
        tt.listen(text)
        m.stop()
        text=""
    elif 'หยุด' in text and ('เพลง' in text or 'เล่น' in text):
        text="หยุดเพลงเรียบร้อยแล้วค่ะ หากต้องการฟังต่อให้สั่ง ฟังต่อได้เลยนะคะ"
        tt.listen(text)
        m.pause()
        text=""
    elif 'เปลี่ยน' in text and 'เพลง' in text:
        text=text.split('เพลง')[1]
        m.change(text)
    elif ('ตอนนี้'in text or 'กำลัง'in text) and 'เล่นเพลง' in text and ('อะไรอยู่'in text or 'อะไร'in text):
        text=text.split('เพลง')[1]
    else:
        text=text+"ระบบยังไม่รองรับค่ะ งั้นเล่นเพลงต่อเลยนะคะ "
        tt.listen(text)
        m.play()
        text=""
    return text

def tum(text:str)->str:
    global s
    
    if ("ฟัง" or "เล่น")in text and 'ธรรมะ'and 'ต่อ' in text: 
        text="เล่นธรรมะต่อแล้วค่ะ"
        s.play()
    elif 'เปิด' in text and 'ธรรมะ' in text:
        text=text.split('ธรรมะ')[1]
        s.change(text)
        #text=text
    elif 'ปิด' in text and ('ธรรมะ' in text or 'เสียง' in text):
        text="ปิดธรรมะเรียบร้อยแล้วค่ะ"
        s.stop()
    elif 'เปลี่ยน' in text and 'ธรรมะ' in text:
        text=text.split('ธรรมะ')[1]
        s.change(text)
    else:
        text="ระบบยังไม่รองรับ กรุณาสั่งงานใหม่ค่ะ "+text
    return text