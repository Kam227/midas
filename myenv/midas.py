import speech_recognition as aa
from gtts import gTTS
import os
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()

def talk(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("afplay output.mp3")  

def input_instruction():
    instruction = "" 
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "midas" in instruction:
                instruction = instruction.replace('midas', '')
            print(instruction)
    except:
        pass
    return instruction

def play_Midas():
    instruction = input_instruction()
    print(instruction)

    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M%p")
        talk("Current time " + time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d /%m /%Y")
        talk("Today's date " + date)
    elif "how are you" in instruction:
        talk("I am fine, how can I assist you?")
    elif 'who is' in instruction:
        human = instruction.replace("who is", "")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    else:
        talk('Sorry, I wasn''t able to hear you')
        pass

play_Midas()