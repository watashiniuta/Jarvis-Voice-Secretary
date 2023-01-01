import speech_recognition as sr
import screen_brightness_control as sbc
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import pyautogui

#google listener 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        print('except worked')
        command = ''
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        command = command.replace('search', '')
        url = 'https://www.google.com/search?q=' + command
        talk('search' + command)
        webbrowser.open(url)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'mute' in command:
        pyautogui.press("volumemute")
        talk('mute')
    elif 'volume up' in command:
        for i in range(0, 7):
            pyautogui.press("volumeup")
        talk('volume up')
    elif 'volume down' in command:
        for i in range(0, 7):
            pyautogui.press("volumedown")
        talk('volume down')
    elif 'brightness' in command and 'increas' in command:
        current_brightness = sbc.get_brightness()
        value = current_brightness[0] + 50
        sbc.fade_brightness(value, increment=10)    
    elif 'brightness' in command and 'decreas' in command:
        current_brightness = sbc.get_brightness()
        value = current_brightness[0] - 50
        sbc.fade_brightness(value, increment=10) 
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' and 'program' in command:
        talk('stop the program')
        return False
    else:
        talk('Please say the command again.')

    return True

running = True
while running:
    running = run_alexa()

print('program was stopped')