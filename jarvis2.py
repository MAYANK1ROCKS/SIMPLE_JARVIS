import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import glob
import jarvisfun

i=0
n=0



        
# recognise===
                                                   # obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("Say something!")
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)


# begin JARVIS 

        if ('goodbye') in message or message=='bye' :                          
            rand = ['A VERY GOOD BYE Boss', 'Jarvis is shutting down','Shutting down sir Mayank']
            jarvisfun.speek(rand,n,mixer)
            break
            
        if ('hello') in message or ('hi') in message or ('hey') in message or ('begin') in message:
            rand = ['Wellcome to Jarvis AI. At your service sir Mayank','hello sir mayank']
            jarvisfun.speek(rand,n,mixer)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['Welcome sir Mayank', 'No mention sir Mayank']
            jarvisfun.speek(rand,n,mixer)

        if  message.lower()=='jarvis':
            rand = ['Yes Sir Mayank? I am listening', 'What can I doo for you sir Mayank?']
            jarvisfun.speek(rand,n,mixer)

        if ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you','I am good Mayank']
            jarvisfun.speek(rand,n,mixer)

        

        if ('your name') in message :
            rand = ['My name is Jarvis at your service sir Mayank']
            jarvisfun.speek(rand,n,mixer)

# other tasks JARVIS ====

        if ('wi-fi') in message:  
            REMOTE_SERVER = "www.google.com"
            jarvisfun.wifi()
            rand = ['We are connected','Connection is established']
            jarvisfun.speek(rand,n,mixer)

        if ('.com') in message  :
            rand = ['Opening' + message,'yes sir i am about to open the '+message]         
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            jarvisfun.speek(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+message)
            print ('opened in google')
            

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords=[]
            for var in querywords:
                if var.lower() not in stopwords:
                    resultwords.append(var.lower())
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = [result+'on google maps']
            print(rand)
            jarvisfun.speek(rand,n,mixer)

        if message != ('start music') and ('start') in message:   
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords=[]
            for var in querywords:
                if var.lower() not in stopwords:
                    resultwords.append(var.lower())
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = [(' mayank i am starting '+result)]
            jarvisfun.speek(rand,n,mixer)

     

    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))