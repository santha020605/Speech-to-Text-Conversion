import speech_recognition as sr

import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    speak("Hi Bro I am your voice assistant. Speak Something!")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)

    while True:
        try:
            print("\nListening....")
            speak("I'm Listening....")

            audio = recognizer.listen(source,timeout=5,phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print("you said :",text)
            speak("you said:"+text)


            if "exit" in text.lower() or "stop" in text.lower():
                speak("Good bye!")
                break

        except sr.WaitTimeoutError:
            print("Timeout : You didn't say anything Broo.")
            speak("I didn't hear anything bro.Please Speak louder again")
            
        except sr.UnknownValueError:
           print("Sorryyy, I didn't catch that "+name+" please say again.")
           speak("sorryyy "+name +" i didn't understand your slang.please Say Again.")

        except sr.RequestError:
           print("Check your internet connection.")
           speak("Sorry "+name+" there's a connection issue.")   
           break

    
