import pyttsx3   #pip install pyttsx3
import datetime #inbuilt
import speech_recognition as sr   #pip install speechRecognition
import pipwin
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''
    this func is for text to speech. it will speak out audio. 
    '''
    # note - below piece of code came from module pyttsx3 init function. 
    # Simply ctrl+click on init and voila!
    engine.say(audio)   
    engine.runAndWait()

def wishme():
    '''
    this func greets.
    '''
    hour = int(datetime.datetime.now().hour) #hour in zero to 23 format
    # if  hour >= 0 and hour < 23:
    if 4 < hour < 12:
        speak("good morning fellas!")
    elif  12 <= hour < 18:
        speak("good noon fellas!")
    elif 18 <= hour < 21 :
        speak("hey good evening!")        
    else:
        speak('good night sleep tight!')

    speak("I am jarvis mam. Please tell me how may I help you?")


def takeCommand_and_print():
    '''
        did pip install pipwin. then did pip install pyaudio as pyaudio was not there earlier.
        this function takes command from user and prints it. (speech to text)

        imported speechRecognition for this func.
    It takes microphone input from the user and returns string output.
    '''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f'user said:{query}\n')

    except Exception as e:
        print(e)
        print("say that again pls...")
        return "None" #None STRING will be returned, mind it STRING is returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # print(server.help()) - this gives help link on smtp
    server.ehlo()
    server.starttls()
    server.login('juileepurohit63@gmail.com', 'your-password')   
    #mentioning my mail id where i wanna login and password for the a/c
    server.sendmail('juileepurohit63@gmail.com', to , content)
    server.close()


if __name__ == "__main__":
    speak("hey you dumbass!")

    # wishme()
    while 1:
    # if 1:   #to run only once
        query = takeCommand_and_print().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query: #this is to search any topic on wikipedia
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:  #this is to open youtube
            webbrowser.open("youtube.com")

        elif "open google" in query:  #this is to open google
            webbrowser.open('google.com')

        elif "open stackoverflow" in query:  #this is to open stackoverflow
            webbrowser.open('stackoverflow.com')

        elif "play song" in query:  #this is to play music
            music_dir = "C:\\Users\\Juilee\\Downloads\\songss"  
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'stop playing song' in query:  #this is to close music player forcefully
            try:                
                os.system("taskkill /f /im Microsoft.Media.Player.exe") # /f - forceful closure, /im- image name i.e. process name #if we do not know name of the running program, simply go to task manager and right click- details- u will get tha name
                #note- taskkill closes all instances of the program
            except Exception as e:
                print(e)

        elif "time" in query:  #this is to get current time
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f"juilee, the time is {strTime}")

        elif 'open vs code' in query:  #this is to open vs code
            codePath = "C:\\Users\\Juilee\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  #backslash for escape sequence
            #how to get this path: start-vs_code-right click-open file location- properties- target
            os.startfile(codePath)

        elif 'send email' in query:  #this is to send email
            try:
                speak("what should I say")  #content of email
                content = takeCommand_and_print()
                to = 'juileepurohit63@gmail.com'
                sendEmail(to, content)  #func to send email
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend, I am not able to send this email")

        elif 'exit' in query:
            exit()

        #add 1 more functionality to this - added closing music player functionality to this