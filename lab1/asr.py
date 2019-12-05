import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
  audio = r.listen(source)
try:
  print("You said " + r.recognize_google(audio,language = "th-TH")) # แสดงข้อความจากเสียงด้วย Google Speech Recognition และกำหนดค่าภาษาเป็นภาษาไทย
except sr.RequestError as e: # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
  print("Could not understand audio")