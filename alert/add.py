from tinydb import TinyDB, Query
import pytz
import datetime as dt
db = TinyDB('./db.json')
d = input("input time  ex 2018-06-29 : ")
t = input("time ex 20:12:01 : ")
text = input("text : ")
timezone = pytz.timezone('Asia/Bangkok')
date_obj = timezone.localize(dt.datetime.strptime(d, '%Y-%m-%d'))# %H:%M:%S
time_obj = t # %H:%M:%S
print(date_obj)
print(time_obj)
print(text)
db.insert({'date': date_obj,'time': time_obj,'text':text, 'alert': True,'duplicate':''})