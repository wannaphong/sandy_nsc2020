# -*- coding: utf-8 -*-
import pafy
import vlc
from vlc import *
import urllib.request
import urllib.parse
import re
Instance = vlc.Instance()

class music:
    def __init__(self):
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_list_player_new()
        #self._search(search)
    def change(self,search):
        self.stop()
        self._search(search)
    def _search(self,search):
        self.query_string = urllib.parse.urlencode({"search_query" : search})
        self.html_content = urllib.request.urlopen("https://www.youtube.com/results?" + self.query_string)
        self.search_results = re.findall(r'href=\"\/watch\?v=(.{11})', self.html_content.read().decode())
        
        self.MediaList= self.Instance.media_list_new()
        for i in self.search_results :
            self.MediaList.add_media("https://www.youtube.com/watch?v=" + i)
        self.player.set_media_list(self.MediaList)
        #self.insex.i >= 0:
        self.player.play()

    def play(self):
        self.player.audio_set_volume(70)
        self.player.play()
    def stop(self):
        self.player.stop()
    def pause(self):
        self.player.pause()
    def next(self):
        self.player.next()
    def mute(self):
        self.player.audio_set_volume(0)
        
    
        

