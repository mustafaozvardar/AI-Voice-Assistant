#pip install SpeechRecognition
#pip install pyttsx3
#pip install pywhatkit
#pip install wikipedia


import speech_recognition as sr 
import pyttsx3
import pywhatkit
import wikipedia
import pyaudio
import datetime


r = sr.Recognizer()
phone_numbers = {"jack": "8561479863", "julia": "6871203984", "martin": "1785693004"}


def speak(command, voice_id=0, rate=135, volume=1.0):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.say(command)
    engine.runAndWait()


def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("--> Listening...")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            #print(my_text)
            

            # hello
            if 'hi' in my_text or 'hello' in my_text:
                speak("Hello, I'm Lara, How can i help you?")
                print("---------------------------------------")
                return True
                

            # ask emotions
            elif 'how are you' in my_text or 'how you doing' in my_text or 'i love you' in my_text:
                speak("I'm an artificial intelligence, I have no feelings and emotions..")
                print("---------------------------------------")
                return True
            
            # see you
            elif 'see you' in my_text:
                speak("Have a nice day..!")
                print("Shut down..")
                return False
            
                
            # ask to play song
            elif 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('playing' + my_text)
                pywhatkit.playonyt(my_text)
                return True


            # ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                print(today)
                speak(today)
                print("---------------------------------------")
                return True
            
          
            # ask time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                print(timenow)
                speak(timenow)
                print("---------------------------------------")
                return True
                

            # ask details about any person
            elif 'who is' in my_text:
                person = my_text.replace('who is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                speak(info)
                print("---------------------------------------")
                return True

            # ask phone number
            elif 'phone number' in my_text:
                names = list(phone_numbers)
                for name in names:
                    if name in my_text:
                        print(name + " phone number is :" + phone_numbers[name])
                        speak(name + " phone number is :" + phone_numbers[name])
                        print("---------------------------------------")
                        return True

            # if not recognized
            else:
                speak("PLease ask correct question...")
                print("---------------------------------------")
                return False


    except:
        print('Error in capturing microphone...!')
        return False


while True:
    if not commands():
        break