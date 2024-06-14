#pyttsx3 is a module which will take care of the libraries required for text to speech conversion.

import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome to my world!")
engine.runAndWait()

