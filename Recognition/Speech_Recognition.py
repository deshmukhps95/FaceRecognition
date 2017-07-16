import speech_recognition as sr
import pyttsx

s_e = pyttsx.init('sapi5')

s_e.setProperty('rate',150)

def Speak(text):
    s_e.say(text)
    s_e.runAndWait();

rec = sr.Recognizer()

def Listen():
    print"in listen"
    with sr.Microphone() as source:
        print("in with")
        audio = rec.listen(source)
    try:
        print "in try"
        return rec.recognize_sphinx(audio)
    except sr.UnknownValueError:
        print "Couldent understand audio"
    except sr.RequestError:
        print "Req error"
    return "";

Speak("Say Something....");

print Listen();

