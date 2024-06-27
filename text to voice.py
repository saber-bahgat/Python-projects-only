import pyttsx3
text= input('Enter the text: ')
engine = pyttsx3.init()
engine.say(text*20)
engine.runAndWait()