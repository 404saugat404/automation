import smtplib
import requests
import json
import speech_recognition as sr
from email.message import EmailMessage
import pywhatkit as p
from googlesearch import search

listener = sr.Recognizer()

dict={
'saugat':'saugat@gmail.com',
'neema':'neema@gmail.com',
'sachin':'shashin@gmail.com',
'sabal':'maharjan@gmail.com'
}



def mic():
    with sr.Microphone() as source:
        print('Program is listening...')
        voice = listener.listen(source)
        try:
            data = listener.recognize_google(voice)
            print(f'You said: {data}')
            return data.lower()
        except sr.UnknownValueError:
            print('Sorry, could not understand the audio.')
            data=None

def send_mail(receiver, subject, message):
    # Your email sending code here
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('sender@gmail.com',' zlkc vutg oouu')    # syntax is server.login('senders mail','app password') for further details, see requirement.txt
    email=EmailMessage()
    email['from']="sender@gmail.com"
    email['to']=receiver
    email['subject']=subject
    email.set_content(message)
    server.send_message(email)

    


def get_weather(city):
    # Your weather API code here
    if city:
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        api_key = 'your pi'
        url = f"{base_url}q={city}&appid={api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            # Save JSON response to a file
            output_file_path = 'weather_data.json'
            with open(output_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
            
            print(f"JSON data saved to: {output_file_path}")
        else:
            print(f"Error: {response.status_code}. Could not retrieve weather data for {city}.")
    else:
        print('No valid city name recognized.')

def play_on_youtube(query):
    p.playonyt(query)

def perform_google_search(query):
    for result in search(query, tld='com', num=10, stop=10, pause=2):
        print(result)

def main_function():
    print("What do you want to do?")
    action = mic()

    if action == "send email":
        print("Whom to send?")
        name = mic()
        print("Received name:", name)

        if name in dict:
            receiver = dict[name]
            print("What is the subject?")
            subject = mic()
            print("Received subject:", subject)

            print("What is the message?")
            message = mic()
            print("Received message:", message)

            send_mail(receiver, subject, message)
            print("Email is sent")
        else:
            print("Name not found in the dictionary.")

    elif action == "get weather":
        print("Which city?")
        city = mic()
        get_weather(city)

    elif action=="play youtube":
        print("What do you want to play on YouTube?")
        query = mic()
        play_on_youtube(query)

    elif action == "google search":
        print("What do you want to search?")
        query = mic()
        perform_google_search(query)

    else:
        print("Invalid action. Please specify a valid action.")

if __name__ == "__main__":
    main_function()
