import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import selenium
from selenium import webdriver
from youtube_search import YoutubeSearch
import sys
import pyautogui
import subprocess
import bs4 
from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen
import GoogleNews
from GoogleNews import GoogleNews
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import tweepy as tw
import time

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
# print(voices[0].id)

firefox_options=Options()

firefox_options.add_argument("user-data-dir=C:\\Program Files\\Mozilla Firefox\\firefox.exe")

driver=webdriver.Firefox(executable_path=r'E:\\PROJECTS\\JARVIS AI ASSISTANT\\geckodriver-v0.26.0-win64\\geckodriver.exe')

consumer_key="YOUR OWN"
consumer_secret="YOUR OWN"
access_token="YOUR OWN"
access_token_secret="YOUR OWN"

engine.setProperty('voice',voices[0].id)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning ")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    elif hour>=18 and hour<24:
        speak("good evening")
    speak("Hi i am issac, I am personal assistant of Jitesh Chawla")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recongining")
        query = r.recognize_google(audio , language="en-in")
        print(f"user said: {query}\n")
    except Exception:
         print(Exception)
         print("say that again ")
         speak("sir, note able to listen, can you please repeat")
         return 'None'
    return query

    


if __name__ == "__main__":
    speak("system on")
    wishme()  
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'who is' in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'play music' in query:
            music_dir="D:\\songs"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))
        elif 'stop music' in query:
            quit()

            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S') 
            speak(f"the time is {strTime}")
        elif ' play Pes' in query:
            code="C:\\Users\\Jitesh Chawla\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        elif 'exit' in query:
            sys.exit()
        
        elif 'screenshot' in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save('D:/screenshot/screenshot.png') 

       
        elif "explorer" in query:
            subprocess.Popen('explorer')
        

        
        
        elif "shutdown" in query:
            speak("turning off computer")
            os.system("shutdown -s")
        
        elif "news" in query:
            news_url="https://news.google.com/news/rss"
            client=urlopen(news_url)
            xml_page=client.read()
            client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list:
                speak(news.title.text)
                speak("-"*60)
        elif "twitter" in query:
            firefox_options=Options()
            webdriver.FirefoxProfile('C:\\Users\\Jitesh Chawla\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\zb7ta375.default-release')
            firefox_options.add_argument("user-data-dir=C:\\Program Files\\Mozilla Firefox\\firefox.exe")
            driver=webdriver.Firefox(executable_path=r'E:\\PROJECTS\\JARVIS AI ASSISTANT\\geckodriver-v0.26.0-win64\\geckodriver.exe')
            driver.get("https://twitter.com/login")
            uname=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
            uname.send_keys("captnpuyol")
            passw=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
            passw.send_keys("elon1511")
            enter=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
            enter.click()
            speak("here is your twitter account sir ")
        
        elif "tweet" in query:
            auth=tw.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token,access_token_secret)
            api=tw.API(auth,wait_on_rate_limit=True)
            
            query=query.replace("tweet","")
            
            print(query)
            api.update_status(query)
            
          
        elif "interstellar" in query:
            os.startfile("D:\\movies\\Interstellar (2014)\\interstellar.mp4")


            


                    


          


        

         



         
      



                 

