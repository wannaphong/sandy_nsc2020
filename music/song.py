# -*- coding: utf-8 -*-
import pafy
import vlc
from vlc import *
import urllib.request
import urllib.parse
import re
from thaitts import TTS
import youtube_dl

tt = TTS()

def youtube(url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(url,download=False)
    if 'formats' in result:
        video = result['formats'][0]
    else:
        video = result
    #print(video)
    return video['url']

def del_d(listdata):
    temp=[]
    for i in listdata:
        if i not in temp:
            temp.append(i)
    return temp

class music:
    def __init__(self):
        self.m=None
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
        for i in del_d(list(self.search_results))[:3]:
            #self.video = pafy.new("https://www.youtube.com/watch?v=" + i)
            #self.streams = self.video.streams
            self.MediaList.add_media(youtube("https://www.youtube.com/watch?v=" + i))#self.streams[-1].url)
        self.player.set_media_list(self.MediaList)
        self.play()

    def setVolume(self, Volume):
        """Set the volume
        """
        self.player.audio_set_volume(Volume)
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
    
    def get_now(self):
        return self.player.get_media_player().get_title()#get_media_player().get_media().get_mrl()

m=music()
s=music()

def song(text:str)->str:
    global m
    if m.m ==  None and 'เปิด' not in text:
        return "คุณยังไม่สั่งเปิดเพลงค่ะ"
    
    elif 'เปิด' in text and 'เพลง' in text:
        text=text.split('เพลง')[1]
        m.change(text)
        m.play()
    elif ("ฟัง" in text or "เล่น"in text) and 'เพลง'and 'ต่อ' in text: 
        text="เล่นเพลงต่อแล้วค่ะ"
        tt.listen(text)
        m.play()
        text=""
    elif 'ปิด' in text and ('เพลง' in text or 'เสียง' in text):
        m.stop()
        text="ปิดเพลงเรียบร้อยแล้วค่ะ"
        tt.listen(text)
        text=""
        m=music()
    elif 'หยุด' in text and ('เพลง' in text or 'เล่น' in text):
        m.pause()
        text="หยุดเพลงเรียบร้อยแล้วค่ะหากต้องการฟังต่อให้สั่งฟังเพลงต่อได้เลยนะคะ"
        tt.listen(text)
        text=""
    elif 'เปลี่ยน' in text and 'เพลง' in text:
        text=text.split('เพลง')[1]
        m.change(text)
    #elif ('ตอนนี้'in text or 'กำลัง'in text) and 'เล่นเพลง' in text and ('อะไรอยู่'in text or 'อะไร'in text):
        
    elif 'เพลง' in text and'ถัดไป' in text:
        m.next()
        text="เล่นเพลงถัดไปแล้วค่ะ"
        tt.listen(text)
        m.play()
        text=""
    else:
        text="ระบบยังไม่รองรับคำสั่ง"+text+"ค่ะ  งั้นเล่นเพลงต่อเลยนะคะ "
        tt.listen(text)
        m.play()
        text=""
    return text

def tum(text:str)->str:
    global s
    
    if s.m ==  None and 'เปิด' not in text:
        return "คุณยังไม่สั่งเปิดธรรมะค่ะ"
    
    elif 'เปิด' in text  and 'ธรรมะ' in text:
        text=text.split('ธรรมะ')[1]
        s.change(text)
        s.play()
    
    
    elif ("ฟัง" in text or "เล่น"in text) and 'ธรรมะ'and 'ต่อ' in text: 
        text="เล่นธรรมะต่อแล้วค่ะ"
        tt.listen(text)
        s.play()
        text=""
    elif 'ปิด' in text and ('ธรรมะ' in text or 'เสียง' in text):
        s.stop()
        text="ปิดธรรมะเรียบร้อยแล้วค่ะ"
        tt.listen(text)
        text=""
        s=music()
    elif 'หยุด' in text and ('ธรรมะ' in text or 'เล่น' in text):
        s.pause()
        text="หยุดธรรมะเรียบร้อยแล้วค่ะหากต้องการฟังธรรมะต่อให้สั่งฟังธรรมะต่อได้เลยนะคะ"
        tt.listen(text)
        text=""
    elif 'เปลี่ยน' in text and 'ธรรมะ' in text:
        text=text.split('ธรรมะ')[1]
        s.change(text)
        tt.listen(text)
        s.play()
        text=""
    
        
    elif 'ธรรมะ' in text and'ถัดไป' in text:
        s.next()
        text="เล่นธรรมะถัดไปแล้วค่ะ"
        tt.listen(text)
        s.play()
        text=""
        
    else:
        text="ระบบยังไม่รองรับค่ะคำสั่ง"+text+"ค่ะ  งั้นเล่นธรรมะต่อเลยนะคะ "
        tt.listen(text)
        s.play()
        text=""
    return text