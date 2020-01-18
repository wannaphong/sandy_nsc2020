# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
from thaitts import TTS
import pytz
import datetime as dt
import time
tts=TTS()
def alert_run():
    db = TinyDB('./db.json')
    N = Query()
    timezone = pytz.timezone('Asia/Bangkok')
    tt = ''
    while True:
        o=str(timezone.localize(dt.datetime.now()).replace(second=0, microsecond=0))
        t=db.search((N.date == o) & (N.alert == True))#db.search(N.date == o)
        if t!=[] and tt!=o:
            temp=t.split("+")[0].split(" ")[-1]
            a="มีการแจ้งเตือน {atime} มีการแจ้งเตือนว่า {text}".format(text=t[0]['text'],atime=str(temp))
            tts.listen(a)
            print(a)
            tt=o

if __name__ == '__main__':
    alert_run()