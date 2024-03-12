import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import google.generativeai as genai
from config import apikey

def ai(prompt):
    genai.configure(api_key=apikey)
    # Model Setup
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        # ... other safety settings (optional)
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    response = model.generate_content(prompt)
    # todo: Wrap this is try catch block
    print(response.candidates[0].content.parts[0].text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(e)
        return "Some Error Occurred. Sorry from RON"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am RON A.I.")
    while True:
        print("Listning")
        query = takeCommand()
        websites = [
            ["Google", "https://www.google.com"],
            ["YouTube", "https://www.youtube.com"],
            ["Facebook", "https://www.facebook.com"],
            ["Baidu", "https://www.baidu.com"],
            ["Wikipedia", "https://www.wikipedia.org"],
            ["Twitter", "https://www.twitter.com"],
            ["Amazon", "https://www.amazon.com"],
            ["Yahoo", "https://www.yahoo.com"],
            ["Instagram", "https://www.instagram.com"],
            ["LinkedIn", "https://www.linkedin.com"],
            ["Pinterest", "https://www.pinterest.com"],
            ["Microsoft", "https://www.microsoft.com"],
            ["Netflix", "https://www.netflix.com"],
            ["Reddit", "https://www.reddit.com"],
            ["Zoom", "https://www.zoom.us"],
            ["Apple", "https://www.apple.com"],
            ["Tencent QQ", "https://www.qq.com"],
            ["Bing", "https://www.bing.com"],
            ["VK", "https://www.vk.com"],
            ["WhatsApp", "https://www.whatsapp.com"],
            ["WeChat", "https://www.wechat.com"],
            ["Microsoft Office", "https://www.office.com"],
            ["Alibaba", "https://www.alibaba.com"],
            ["Stack Overflow", "https://stackoverflow.com"],
            ["TikTok", "https://www.tiktok.com"],
            ["Messenger", "https://www.messenger.com"],
            ["Google Maps", "https://www.google.com/maps"],
            ["GitHub", "https://github.com"],
            ["Google Play", "https://play.google.com"],
            ["Snapchat", "https://www.snapchat.com"],
            ["Adobe", "https://www.adobe.com"],
            ["DuckDuckGo", "https://duckduckgo.com"],
            ["IMDb", "https://www.imdb.com"],
            ["Yandex", "https://www.yandex.com"],
            ["WordPress", "https://www.wordpress.com"],
            ["Google Drive", "https://drive.google.com"],
            ["Telegram", "https://telegram.org"],
            ["Office 365", "https://www.office.com"],
            ["PayPal", "https://www.paypal.com"],
            ["Amazon Prime", "https://www.amazon.com/prime"],
            ["Yahoo Mail", "https://mail.yahoo.com"],
            ["Booking.com", "https://www.booking.com"],
            ["Google Translate", "https://translate.google.com"],
            ["Quora", "https://www.quora.com"],
            ["Twitch", "https://www.twitch.tv"],
            ["Walmart", "https://www.walmart.com"],
            ["Microsoft Teams", "https://www.microsoft.com/en-us/microsoft-365/microsoft-teams/group-chat-software"],
            ["Google Docs", "https://docs.google.com"],
            ["Roblox", "https://www.roblox.com"],
            ["Medium", "https://medium.com"],
            ["Microsoft Edge", "https://www.microsoft.com/en-us/edge"],
            ["Discord", "https://discord.com"],
            ["Blogger", "https://www.blogger.com"],
            ["Amazon Web Services", "https://aws.amazon.com"],
            ["ESPN", "https://www.espn.com"],
            ["Fandom", "https://www.fandom.com"],
            ["Gmail", "https://mail.google.com"],
            ["BBC", "https://www.bbc.co.uk"],
            ["Etsy", "https://www.etsy.com"],
            ["BBC News", "https://www.bbc.com/news"],
            ["MSN", "https://www.msn.com"],
            ["Hulu", "https://www.hulu.com"],
            ["Craigslist", "https://www.craigslist.org"],
            ["Google Scholar", "https://scholar.google.com"],
            ["Microsoft Store", "https://www.microsoft.com/en-us/store/b/home"],
            ["The New York Times", "https://www.nytimes.com"],
            ["The Guardian", "https://www.theguardian.com"],
            ["Naver", "https://www.naver.com"],
            ["Dailymotion", "https://www.dailymotion.com"],
            ["ESPNcricinfo", "https://www.espncricinfo.com"],
            ["BBC Weather", "https://www.bbc.co.uk/weather"],
            ["The Weather Channel", "https://weather.com"],
            ["CNN", "https://www.cnn.com"],
            ["NBC News", "https://www.nbcnews.com"],
            ["The Washington Post", "https://www.washingtonpost.com"],
            ["The Economist", "https://www.economist.com"],
            ["Vimeo", "https://vimeo.com"],
            ["Microsoft Office 365", "https://www.microsoft.com/en-us/microsoft-365"],
            ["Hdfc Netbanking", "https://netbanking.hdfcbank.com"],
            ["Hdfc Netbanking Login", "https://netbanking.hdfcbank.com/netbanking"],
            ["Flipkart", "https://www.flipkart.com"],
            ["Google Classroom", "https://classroom.google.com"],
            ["MSN Weather", "https://www.microsoft.com/en-us/p/msn-weather/9wzdncrfj3q2"],
            ["NBC News", "https://www.nbcnews.com"],
            ["Web WhatsApp", "https://web.whatsapp.com"],
            ["The Washington Post", "https://www.washingtonpost.com"],
            ["The Economist", "https://www.economist.com"],
            ["Flipkart", "https://www.flipkart.com"],
            ["Google Classroom", "https://classroom.google.com"],
            ["Web WhatsApp", "https://web.whatsapp.com"],
            ["Google Meet", "https://meet.google.com"],
            ["Twitch App", "https://www.microsoft.com/en-us/p/twitch/9nblggh5x1sl"],
            ["Linkedin App", "https://www.microsoft.com/en-us/p/linkedin/9wzdncrfj3wt"],
            ["Quora App", "https://www.microsoft.com/en-us/p/quora/9wzdncrfj55n"],
            ["Twitter App", "https://www.microsoft.com/en-us/p/twitter/9wzdncrfj140"],
            ["Linkedin Learning App", "https://www.microsoft.com/en-us/p/linkedin-learning/9nwpjln511g4"],
            ["Bbc News App", "https://www.microsoft.com/en-us/p/bbc-news/9wzdncrfj52h"],
            ["Linkedin Jobs", "https://www.linkedin.com/jobs"],
            ["Linkedin Sales Navigator", "https://www.linkedin.com/sales"],
            ["Linkedin Login Page", "https://www.linkedin.com/login"],
            ["Linkedin Learning", "https://www.linkedin.com/learning"],
            ["Linkedin Sign Up", "https://www.linkedin.com/signup"],
            ["Linkedin Premium", "https://www.linkedin.com/premium"]
        ]
        for site in websites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        if "Open Music".lower() in query.lower():
            os.startfile("D:\Music\Jamie Duffy - Solas (Official Video).mp3")
                # break

        if "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir time is {strfTime}")

        if "open spotify".lower() in query.lower():
            os.startfile(r"C:\Users\91905\AppData\Roaming\Spotify\spotify.exe")

        if "Using Google Gemini".lower() in query.lower():
            ai(prompt=query)
            # say(query)
            # break
