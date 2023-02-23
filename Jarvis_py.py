import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import requests
import wikipedia
import webbrowser
import pywhatkit
import email
import smtplib
import details as dd
import pyautogui
import playsound
from playsound import playsound
from bs4 import BeautifulSoup
import PyPDF2
from gtts import gTTS
import googletrans
import pdfreader
from time import sleep




engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

#print(voice[0].id)


# Text to speech conversion
def speak(audio):
   engine.say(audio)
   engine.runAndWait()
   print(audio)

# Speech to Text conversion
def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 10
        audio = r.listen(source,timeout=10,phrase_time_limit=20)

    try:
        print('Recognizing........')
        query = r.recognize_google(audio,language="en-US")
        print(f"User Said = {query}")
    
    except Exception as e:
        speak('Say that again please.....')
        return 'none'
    return query

# To wish == Create wish such GM,Good evening by jarvis
def wish():
    hour = int(datetime.datetime.now().hour) # it will deliver current time in min and hours.

    if hour >= 0 and hour <= 12:
        speak("Good Morning Sir ")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon Sir") 
    else:
        speak(f"Good Evening Sir")
    speak('Hello Sir,my name is JARVIS, please can you tell me what can I do for you?')




def sendEmail (to,content):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.login(dd.emailID,dd.emailpassword)
    s.sendmail(dd.emailID,to,content)
    s.quit()

def temperature():
    search = 'temperature in talegaon dabhade'
    Url = (f'https://www.google.co.in/search?q={search}')
    a = requests.get(Url)
    data = BeautifulSoup(a.text,'html.parser')
    temperature = data.find('div',class_ = 'BNeawe').text
    speak(f'the temperature is {temperature} celsius')

def pdf_reader():

      
        book = open('D:/python_hw/The Monk who sold his ferrari - Robin Sharma (PDF) [Qwerty80].pdf','rb')
        pdfreader = PyPDF2.PdfReader(book)
        pages = len(pdfreader.pages)
        speak(f'The total numbers of pages in this book {pages}')
        speak('Sir please enter the page number so that I can read')
        pg = int(input('Please enter the page number:'))
        page = pdfreader.pages[pg]
        text_t = page.extract_text()
        speak(text_t)
  






if __name__ == "__main__":
    wish()
    #while True:
    if 1:

        query = takecommand().lower()

        # logic building for tasks

        if 'open notepad' in query:
            apath = ('C://Program Files//WindowsApps//Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe//Notepad//Notepad.exe')
            os.startfile(apath)
        
        elif 'open pdf' in query:
            bpath = ("C:/Users/Public/Desktop/Adobe Acrobat.lnk")
            os.startfile(bpath)

        elif 'open microsoft word' in query:
            cpath = ("C:/Users/GANESH THORBOLE/word.lnk")
            os.startfile(cpath)
        
        elif 'open microsoft excel' in query:
            dpath = ("C:/Users/GANESH THORBOLE/Excel.lnk")
            os.startfile(dpath)
        
        elif 'open microsoft one note' in query:
            epath = ("C:/Users/GANESH THORBOLE/OneNote.lnk")
            os.startfile(epath)

        elif 'open microsoft powerpoint' in query:
            g = ("C:/Users/GANESH THORBOLE/PowerPoint.lnk")
            os.startfile(g)

        

       
    
        elif 'open command prompt' in query:
            os.system('start cmd')
        
        elif 'play music' in query:
            music_dir = ("C:/Users/GANESH THORBOLE/Music")
            songs = os.listdir(music_dir)
            Random = random.choice(songs)
            os.startfile(os.path.join(music_dir,Random))

        elif 'ip address' in query:
            from requests import get
            ip = get('https://api.ipify.org').text
            speak(f'Dear sir your respected IP address is {ip}')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia......')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            speak(results)
            print(results)

        elif 'open youtube' in query:
           webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            speak('Sir what google search can I do it for you?')
            cmd = takecommand().lower()
            webbrowser.open(f'{cmd}')

        
        elif 'open chrome' in query:
            webbrowser.open('https://www.google.co.in')

       
        elif 'open stack overflow' in query:
            webbrowser.open('https://www.stackoverflow.com')

        elif 'open github' in query:
            webbrowser.open('https://www.github.com')
        
        elif 'send message' in query:
            import pywhatkit as kit
            kit.sendwhatmsg(f"+919881821696",'Hello How are you',20,00)
        
        elif 'play songs on youtube' in query:
           import pywhatkit as kit
           speak('What songs can I play for you?')
           cmd = takecommand().lower()
           kit.playonyt(f'{cmd}')
           
    
        elif 'open facebook' in query:
            webbrowser.open('https://www.facebook.com')

        elif 'email to ganesh' in query:
            try:
                speak('What Shall I say?')
                content = takecommand().lower()
                to = ('g.thorbole@gmail.com')
                sendEmail(to,content) 
                speak('email has been sent to ganesh')

            except Exception as e:
                print(e)
        
        elif 'open time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M')
            speak(f'Sir The Current time is {strTime}')

      
# to close any application:
        elif 'close notepad' in query:
            speak('ok sir,I am closing notepad now')
            os.system('taskkill /im notepad.exe')

        elif 'close chrome' in query:
            speak('ok sir,I am closing chrome now')
            os.system('taskkill /im chrome.exe')
        
    

# to set an alarm:222
        elif 'set alarm' in query:
            speak('Sir Please Enter your alarm Time !')
            time = input(': Enter Time :')
            
            
            while True:
                Time_ac = datetime.datetime.now()
                now = Time_ac.strftime('%H:%M:%S')

                if now == time:
                    speak(f"Time to wake up Sir!!")
                    playsound("submarine.mp3")
                   

                elif now>time:
                    break
# to set tmeperature:
        elif 'temperature' in query:
            temperature()      
# to read audiobook:
        elif 'read pdf' in query:
            pdf_reader()
   
# to shutdown the laptop
        elif 'shutdown' in query:
            speak('Do you really want to shutdown')
            reply = takecommand()
            if 'yes' in reply:
                os.system('shutdown /s /t 1')
            else:
                'break'

        elif 'sleep' in query:
            speak('Do you really want to sleep')
            reply = takecommand()
            if 'yes' in reply:
                os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            else:
                'break'
          

      
         
# to restart the laptop
        elif 'restart' in query:
            speak('Do you really want to restart')
            reply = takecommand()
            if 'yes' in reply:
                os.system('shutdown /r /t 1')
            else:
                'break'

# to translate document in python.      
        elif 'change in language' in query:
            translated_text = (f'https://translate.google.com/?sl=en&tl=de&text={next}')
            webbrowser.open(translated_text)
          
        
                


        


        
            
       


           
   









      
            

        
       

            





















if __name__ == '__main__':
    takecommand()
   #speak('Hello   Hello Sir')




'''
query = query.replace('translate', '')
query = query.replace('in marathi','')
from googletrans import Translator
translate(query)
'''

'''
import pywhatkit as kit
           speak('What songs can I play for you?')
           cmd = takecommand().lower()
           kit.playonyt(f'{cmd}')
           
  translated_text = (f'https://translate.google.com/?sl=en&tl=de&text={next}')
            webbrowser.open(translated_text)
          
import pywhatkit as kit
            kit.sendwhatmsg("+919881821696",'Hello This is a message delivered from Python',22,12)

'''
