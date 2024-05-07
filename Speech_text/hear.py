import speech_recognition
import pyttsx3


hear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
        print(" I'm listening ")
        audio = hear.listen(mic)
you = hear.recognize_google(audio,language='vi-VI')
print(you)
