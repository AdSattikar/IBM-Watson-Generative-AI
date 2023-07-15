import win32com.client
import speech_recognition as sr
import webbrowser
import datetime

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print(text)
    speaker.Speak(text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return f"Some Error Occured: {e}"

if __name__ == '__main__':
    print("Welcome Adnan")
    say("Hello I am your Desktop Assistant")
    while True:
        print("Listening...")
        query = listen()
        sites = [["youtube","https://youtube.com"],["google" , "https://google.com"],["wikipedia","https://wikipedia.com"],["chat gpt","chat.openai.com"],["aqua treat","https://aquatreatsystems.netlify.app"]]
        
        for site in sites: 
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])

        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strTime}")

        else:
            say(query)