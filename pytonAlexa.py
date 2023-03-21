import speech_recognition as benis_alex
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = benis_alex.Recognizer() 
#engine that initializes text to speech
engine = pyttsx3.init()
#get all the voices
voices = engine.getProperty('voices')
#choose voice index 1 that is female voice
engine.setProperty('voice', voices[0].id)

def talking(text):
    engine.say(text)
    engine.runAndWait()
def except_the_commands():
    try:
        #use the mic to be your source and the listener listen to the mic that its the source
        with benis_alex.Microphone() as source:
            #while google is listening on the microphone written alexa listening
            print('Now ALex is listening')
            voice = listener.listen(source)
            #here i give to google recognize to listen to my voice and recognize what i say
            #we using google api to give as text from our voice
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alex' in command:
                #i change the text alex in ' ' .
                command = command.replace('alex', '')
                # talking(command)
                print(command)
    except:
        pass
    return command 

def alex_running():
    command = except_the_commands()
    print(command)
    if 'play' in command:
        song_order_play = command.replace('play', '')
        talking('playing' + song_order_play)
        pywhatkit.playonyt(song_order_play)
        print(song_order_play)
    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        print(time_now)
        talking('The time now is ' + time_now)
    elif 'who is' in command:
        serch_person = command.replace('who is', '')
        info = wikipedia.summary(serch_person, 3)
        print(info)
        talking(info)


while True:
    alex_running()