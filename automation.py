import speech_recognition as sr
from selenium import webdriver
import time
import json
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()


def funAutomation():
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source:
            print('Active...')
            print("adjusting audio please wait...")
            r.adjust_for_ambient_noise(source)
            print("please speak")
            audio = r.listen(source)

            # Using google to recognize audio
            MyText = r.recognize_google(audio,language='en-IN', show_all=False)

            print(MyText)
            if MyText == 'Oggy open YouTube':
                driver = webdriver.Chrome()
                driver.get('https://youtube.com')
                search = driver.find_element_by_xpath('//*[@id="search"]')
            elif MyText == 'Oggy open Google':
                driver = webdriver.Chrome()
                driver.get('https://google.com')
                audio = r.listen(source)
                # Using google to recognize audio
                print('Say something to search...')
                print('listening...')
                googlesearch = r.recognize_google(audio,language='en-IN', show_all=False)
                srTxt = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                srTxt.send_keys(googlesearch)
                print(googlesearch)
                searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
                searchButton.click()
            elif MyText == 'Stop' or MyText == 'stop':
                exit(100)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        funAutomation()


while True:
    funAutomation()
    time.sleep(1)
    print('sleeping...zzzz')

