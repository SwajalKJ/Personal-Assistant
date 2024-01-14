import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import os


def speech_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Sorry... Can You Repeat It")

def speech_to_text(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    speech_to_text("Hello, I am your Personal Assistant")
    #print("Hello, I am your Personal Assistant")   
    while True:
        Text = speech_text().lower()
        sites = [["youtube", "https://www.youtube.com/"], ["wikipedia",'https://www.wikipedia.org/'],
                ["google","https://www.google.com/"], ["github", "https://github.com/"]]
        for site in sites:
            if f"Open {site[0]}".lower() in Text:
                speech_to_text(f"opening {site[0]}")
                webbrowser.open(site[1])

        if "current time" in Text:
            time = datetime.datetime.now().strftime("%I%M%p")
            speech_to_text(f"current time is: {time}")
        elif "jokes" in Text:
            joke = pyjokes.get_jokes(language = "en" , category = "all")
            print(joke)
            speech_to_text(f"Here is a joke for you: {joke}")
        elif "play song" in Text:
            path = "C:/Users/jhasw/Music/"
            listsong = os.listdir(path)
            speech_to_text("Playing some songs")
            os.startfile(os.path.join(path , listsong[1]))
        elif "close" in Text:
            speech_to_text("Thank you, See you soon")
            break
