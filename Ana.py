from pynput import keyboard
import pyttsx3
import speech_recognition as speechrec
import datetime
import wikipedia
import webbrowser
import os
import requests
from selenium import webdriver
from pynput.keyboard import Key,Controller
import math
import pyjokes 


speechEngine = pyttsx3.init('sapi5')
voices = speechEngine.getProperty('voices')
speechEngine.setProperty('voice', voices[1].id)

def speak(audio):
    speechEngine.say(audio)
    speechEngine.runAndWait()
  
def greet():
    hour = int(datetime.datetime.now().hour)

    if(hour>=0 and hour<12):
        speak("Good Morning!")

    elif(hour>=12 and hour<16):
        speak("Good Afternoon!")

    elif(hour>=16 and hour<24):
        speak("Good Evening!")

    # elif(hour>=20 and hour<24):
        # speak("Good Night!")
    
    speak("How can I help you?")

def takeQuery():
    r = speechrec.Recognizer()
    with speechrec.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")

    except Exception as e:
        # print(e)
        print("Couldn't recognise that...try again")
        return "None"
    return query

greet()
while (True):
    query = takeQuery().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace('wikipedia','')
        result = wikipedia.summary(query, sentences=2)
        speak('According to wikipedia..')
        print(result)
        speak(result)
    
    elif "open web browser" in query:
        speak("opening web browser")
        webbrowser.open("http://google.com")

    elif "images" in query:
        speak('searching google images')
        query = query.replace('search','')
        query = query.replace('on','')
        query = query.replace('google','')
        query = query.replace('images','')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com/imghp?hl=en')
        searchBox = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
        searchBox.send_keys(query)
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    
    elif "google" in query:
        speak('searching google')
        query = query.replace('search','')
        query = query.replace('on','')
        query = query.replace('google','')
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        searchBox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        searchBox.send_keys(query)
        # searchButton = driver.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.lJ9FBc > center > input.gNO89bbody > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.lJ9FBc > center > input.gNO89bbody > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.UUbT9 > div.aajZCb > div.lJ9FBc > center > input.gNO89b')
        # searchButton.click()
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
      
    elif "youtube" in query:
        speak('searching youtube')
        query = query.replace('search','')
        query = query.replace('on','')
        query = query.replace('youtube','')
        driver = webdriver.Chrome()
        driver.get('https://www.youtube.com/')
        searchBox = driver.find_element_by_xpath('//*[@id="search"]')
        searchBox.send_keys(query)
        searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
        searchButton.click()

    elif "open email" in query:
        speak("opening gmail")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

    elif "whatsapp" in query:
        speak("opening whatsapp")
        webbrowser.open("https://web.whatsapp.com/")

    elif "the time" in query:
        time_ = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {time_}")
        
    elif "weather" in query:
        user_api = os.environ['weather_data'] 
        location = 'bangalore'
        api_link = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}" 
        request_link = requests.get(api_link)
        api_data = request_link.json()
        # print(api_data)

        city_weather = (api_data['weather'][0]['main'])
        city_temp = str(math.floor(api_data['main']['temp'] - 273.15))

        if city_weather == 'Clear':
            speak('the weather is clear today with a temperature of '+city_temp+' degree celsius')
        elif city_weather == 'Clouds':
            speak('the weather is cloudy today with a temperature of '+city_temp+' degree celsius')
        elif city_weather == 'Rain':
            speak('the weather is rainy today with a temperature of '+city_temp+' degree celsius')

    elif "music" in query:
        speak('playing')
        m_dir = 'E:\Music'
        songs = os.listdir(m_dir)
        # print(songs)
        os.startfile(os.path.join(m_dir, songs[0]))
    
    elif "joke" in query:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    
