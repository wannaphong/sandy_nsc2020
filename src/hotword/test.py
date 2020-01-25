# -*- coding: utf-8 -*-
import time
import winsound
from precise_runner import PreciseEngine, PreciseRunner

print('start')
def on_prediction(prob):
    print(print(prob) if prob > 0.5 else '.', end='', flush=True)

def on_activation():
    print('Activation')
    winsound.PlaySound("*", winsound.MB_OK)

engine = PreciseEngine('C:\\Users\\TC\\Anaconda3\\Scripts\\precise-engine.exe', 'jao-sandy.pb') 
# PreciseEngine(ที่ตั้งโฟลเดอร์ Scripts ของ precise-engine ,  ไฟล์ model)
# หากรันบน Linux ใช้ precise-engine/precise-engine ใน precise-engine
runner = PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation, trigger_level=0)
runner.start()

while 1:
    time.sleep(1)