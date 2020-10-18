import random
from datetime import datetime
import requests

def greet():
    response = [
        "Welcome, I am chatbot.Your name please",
        "Hey hello! I am your bot who helps you to do calculations.May I know your name?"
    ]
    print(random.choice(response))

def get_greeting_time():
    time = datetime.now()
    greeting_time = "Good Morning"
    if(time.hour > 12 and time.hour <= 17):
        greeting_time = "Good Afternoon"
    elif(time.hour > 17 and time.hour < 22):
        greeting_time = "Good Evening"
    elif(time.hour >= 22):
        greeting_time = "Hi, Its late"
    return greeting_time

def welcome(name):
    message = [
        "Nice to meet you",
        "Lets work together"
    ]
    print(f"{get_greeting_time()}, {random.choice(message)}")

def menu():
    print("1. Calculate given expression")
    print("2. Weather Report of given City")
    print("3. Exit")
    print("__________________________________")
    try:
        return int(input("Enter your choice : "))
    except Exception as e:
        print("Something went wrong")
        return 0

def evaluate_expr():
    expr = input("Enter expression : ")
    try:
        print("Final Result : ", eval(expr))
    except:
        print("Please enter valid expression")

def weather_report():
    city = input("Enter city name : ")
    weather_data = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=f134f22602331d98954eaf7586ce4265&q="+city).json()
    try:
        print("Present_Temparature : ",weather_data['main']['temp'])
        print("Wind_Speed : ",weather_data['wind']['speed'])
        print("Humidity : ",weather_data['main']['humidity'])
        # print(weather_data)
    except:
        print("Something is wrong")


def bot():
    greet()
    name = input("Enter your name : ")
    welcome(name)
    choice = menu()
    while choice != 3:
        if choice == 1:
            evaluate_expr()
        elif(choice == 2):
            weather_report()
        choice = menu()
bot()