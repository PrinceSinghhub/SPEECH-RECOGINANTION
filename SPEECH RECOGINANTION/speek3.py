import speech_recognition as s
from win32com.client import Dispatch
sr=s.Recognizer()
print("Speek what you want .................")
with s.Microphone() as m:
    audio=sr.listen(m)
    q=sr.recognize_google(audio,language='eng-in')
    print(q)
speak = Dispatch("SAPI.Spvoice")
speak.Speak(q)