from precise_runner import PreciseRunner, PreciseEngine
from threading import Event

def on_prediction(prob):
    print('!' if prob > 0.5 else '.', end='', flush=True)

def on_activation():
    print("ok")

engine = PreciseEngine('C:\\Users\\TC\\Anaconda3\\Scripts\\precise-engine.exe', 'jao-sandy.pb') 
PreciseRunner(engine, on_prediction=on_prediction, on_activation=on_activation,
              trigger_level=0).start()
Event().wait()  # Wait forever