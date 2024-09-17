import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import requests
import wikipedia
import webbrowser
import pywhatkit as kit
import json
# from pyChatGPT import ChatGPT
import subprocess
import json
import difflib as d
import os
import requests
# import Armenia as a

import google.generativeai as genai
from dotenv import load_dotenv


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def default():
        
       
            print("listening......")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                # speak("Listening, sir.")
                speak("I am listening")
                print("Listening....")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                try:
                
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    print("Recognizing.....")
                    val = r.recognize_google(audio, language="en-in")
                    # print(f"User said: {query}")

                except sr.WaitTimeoutError:
                    
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                    # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")
                        return val
                    
                except sr.UnknownValueError:
                    
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")
                        return val
                except sr.RequestError as e:
                    
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                    
                    
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")
                        return val
                except:
                    print("listening......")
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                # speak("Listening, sir.")
                        print("Listening....")
                        r.pause_threshold = 1
                        r.adjust_for_ambient_noise(source)
                    
                    
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        print("Recognizing.....")
                        val = r.recognize_google(audio, language="en-in")

        
        
            return val


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening, Subhayan.")
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
        except sr.WaitTimeoutError:
            speak("I didn't catch that. Please try again.")
            return "none"
        except sr.UnknownValueError:
            speak("I didn't understand that. Please try again.")
            return "none"
        except sr.RequestError as e:
            speak("Could not request results; check your network connection.")
            print(f"Could not request results; {e}")
            return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak('''hey subhayan,
          I am Adrika, please tell me how can I help you''')

if __name__ == "__main__":
  
    e=default().lower()

    if e=="wake up":
          wish()
          while True:
            query = take_command().lower()
            if "google" in query:
                os.system("start https://www.google.com")
            elif "calculator" in query:
                speak("Opening Calculator")
                os.system("calc")
            elif "command prompt" in query or "cmd" in query:
                speak("Opening Command Prompt")
                os.system("start cmd")
            elif "notepad" in query:
                speak("opening notepad")
                os.system("notepad")
            elif "powerpoint" in query:
                speak("opening powerpoint")
                os.startfile("powerpnt")

            elif "love" in query:
                speak('''i love you too my baby.You are my life sona''')
            elif "code" in query:
                speak("opening vscode")
                os.startfile("C:\\Users\\subha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif "open camera" in query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret,img =cap.read()
                    cv2.imshow("webcam",img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif "ip address" in query:
                ip=requests.get("https://api.ipify.org").text
                speak(f"your id address is {ip}")
                print(f"your id adddress is {ip}")
            elif "wikipedia" in query:
                speak("searching wikipedia")
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)
                
            elif"open youtube" in query:
                webbrowser.open("www.youtube.com")
            elif"open stackoverflow" in query:
                webbrowser.open("www.stackoverflow.com")
            elif"open facebook" in query:
                webbrowser.open("www.facebook.com")
            elif "search" in query:
                cm=take_command().lower()
                webbrowser.open(f"{cm}")
            elif"send message" in query:
                
                speak("What is the message?")
                cm = take_command().lower()
                try:
                        
                        kit.sendwhatmsg_instantly("+9477033200", cm)
                        speak("Message has been sent")
                except Exception as e:
                    speak("An error occurred while sending the message")
                    cm=take_command().lower()
                    kit.sendwhatmsg_instantly("9477033200",cm)
            elif"music" in query:
                speak("what music would you like to hear")
                cm=take_command().lower()
                kit.playonyt(cm)
                speak("enjoy your music sir")
                break
            elif"play video on youtube" in query:
                speak("what video would you like to see sir")
                cm=take_command().lower()
                kit.playonyt(cm)
                speak("enjoy your video sir")
                break
            elif"news" in query:
                
                speak("which news do you want to hear")
                cm=take_command().lower()
               
                
                r=requests.get(f"https://newsapi.org/v2/everything?q={cm}&from=2024-07-22&to=2024-07-22&sortBy=popularity&apiKey=e733a5ee87f74b24916cd362109f2739")
                j=json.loads(r.text)
                k=0
                for i in j["articles"]:
                    speak(i["title"])
                    speak(i["description"])
                    print(i["title"])
                    print(i["description"])
                    print("------------------------------------------------------------------------------")
                    k=k+1
                    if(k==5):
                        speak(f"thats all about {cm}")
                        break
            elif "help" in query:
               while True:
                speak("what is your question")
                cm=take_command().lower()
                # cm.replace()
                if cm=="thank you" or cm=="no":
                    speak('''you are welcome
                          any time feel free to ask''')
                    break
                
                genai.configure(api_key=os.getenv("api_key"))

    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
                generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                                        }
                

                model = genai.GenerativeModel(
                        model_name="gemini-1.5-pro",
                        generation_config=generation_config,
                        # safety_settings = Adjust safety settings
                        # See https://ai.google.dev/gemini-api/docs/safety-settings
                        )
                
                
                chat_session = model.start_chat(
                        history=[
                        ]
                        )
                response = chat_session.send_message(cm)
                print(response.text)

                speak(response.text.replace("*","").replace("#",""))
                speak("any other question sir")

          
                    
                    



            elif "cpp" in query:
                speak("opening devc++")
                os.startfile("C:\\Program Files (x86)\\Embarcadero\\Dev-Cpp\\devcpp.exe")
                speak("enjoy your code sir")
                break

            elif "translate" in query:
                
            #  word=takecommand().lower()
            #  translate(word)


                
                speak("tell the word you want to search: ")
                word=take_command().lower()
                
                j=json.load(open("data.json"))
                def translate(w):
                    if w in j.keys():
                        print(j[w])
                    elif d.get_close_matches(w,j.keys()):
                        print(f"did you mean this {d.get_close_matches(w,j.keys())[0]}")
                        speak(f"did you mean this {d.get_close_matches(w,j.keys())[0]}")
                        print(f"then the word meaning is {j[d.get_close_matches(w,j.keys())[0]]}")
                        speak(f"then the word meaning is {j[d.get_close_matches(w,j.keys())[0]]}")

                    else:
                        print("the word is not found")
                        speak("the word is not found")
                
                translate(word)

    # print(translate('ca'))
            elif "flag" in query:
                speak("which country flag do you want to see")
                cm=take_command().lower()
                if cm=="armenia":
                    speak(f"flag of {cm}")
                    import Armenia
                    Armenia.func()
                    # break
                if cm=="india":
                    speak(f"flag of {cm}")
                    import indian_flag as ind
                    ind.func()
                    # break
                if cm=="japan":
                    speak(f"flag of {cm}")
                    import japan_flag as japan
                    japan.func()
                    # break
                if cm=="russia":
                    speak(f"flag of {cm}")
                    import Russia
                    Russia.func()
                    # break
                if cm=="netherlands":
                    speak(f"flag of {cm}")
                    import netherlands as n
                    n.func()
                if cm=="poland":
                    speak(f"flag of {cm}")
                    import poland
                    poland.func()
                if cm=="germany":
                    speak(f"flag of {cm}")
                    import germany
                    germany.func()

                          






            

            elif "weather" in query:
                speak("which city weather update do you want to hear")
                city=take_command().lower()
                api_key="4e5f1dbfe280ccb6c3576630c8488dc4"

                weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
                p=weather.json()
# print(p.keys())
                print(f"today's weather in {city} is {p["weather"][0]["main"]}")
                speak(f"today's weather in {city} is {p["weather"][0]["main"]}")
                print(f"today's temperature in {city} is {p['main']['temp']}")
                speak(f"today's temperature in {city} is {p['main']['temp']}")


            
            elif "exit" in query or "stop" in query:
                speak('''Goodbye, sir
                    Please come again''')
                break
        # Add more commands here
