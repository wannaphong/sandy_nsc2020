import pafy
import vlc
from vlc import *
import urllib.request
import urllib.parse
import re


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

def song(text:str)->str:
    global m
    
    if "ฟัง" in text and 'ต่อ' in text: 
        text="เล่นเพลงต่อแล้วค่ะ"
        m.play()
    elif 'เปิด' in text and 'เพลง' in text:
        text=text.split('เพลง')[1]
        m.change(text)
        #text=text
    elif 'ปิด' in text and ('เพลง' in text or 'เสียง' in text):
        text="ปิดเพลงเรียบร้อยแล้วค่ะ"
        m.stop()
    else:
        text="ระบบยังไม่รองรับ กรุณาสั่งงานใหม่ค่ะ "+text
    return text

def tum(text:str)->str:
    global m
    
    if "ฟัง" in text and 'ต่อ' in text: 
        text="เล่นธรรมะต่อแล้วค่ะ"
        m.play()
    elif 'เปิด' in text and 'ธรรมะ' in text:
        text=text.split('ธรรมะ')[1]
        m.change(text)
        #text=text
    elif 'ปิด' in text and ('ธรรมะ' in text or 'เสียง' in text):
        text="ปิดธรรมะเรียบร้อยแล้วค่ะ"
        m.stop()
    else:
        text="ระบบยังไม่รองรับ กรุณาสั่งงานใหม่ค่ะ "+text
    return text