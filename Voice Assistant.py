import win32com.client
import speech_recognition as sr
import webbrowser
import datetime
import openai
import os
import requests
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

chatStr=""

def ai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    text = f"OpenAI response for Prompt: {''.join(prompt.split('intelligence')[1:]).strip()} \n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
   
    text += response["choices"][0]["text"]

    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")
    
    with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)

def chat(query):
    global chatStr
    openai.api_key = os.getenv("OPENAI_API_KEY")
    chatStr += f"Adnan:{query} \n Assistant: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
            return query
        except Exception as e:
            return f"Some Error Occured: {e}"

def get_news_headlines():
    news_api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={news_api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data["articles"]

    headlines = []
    for article in articles[0:10]:
        title = article["title"]
        headlines.append(title)

    return headlines
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

        elif "Using Artificial Intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "news" in query.lower() or "headlines" in query.lower():
            headlines = get_news_headlines()
            news_response = "\n".join(headlines)
            say(news_response)
            
        elif "stop talking".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)