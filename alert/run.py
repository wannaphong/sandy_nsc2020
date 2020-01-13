# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
import pytz
import datetime as dt
import time
db = TinyDB('./db.json')
N = Query()
timezone = pytz.timezone('Asia/Bangkok')
tt = ''
while True:
    o=str(timezone.localize(dt.datetime.now()).replace(second=0, microsecond=0))
    t=db.search((N.date == o) & (N.alert == True))#db.search(N.date == o)
    if t!=[] and tt!=o:
        print(t[0]['text'])
        tt=o