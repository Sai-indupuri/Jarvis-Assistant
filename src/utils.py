import os
import requests
import time
import threading
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv()

# Weather API
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        response = requests.get(WEATHER_BASE_URL, params=params)
        data = response.json()
        
        if data['cod'] != 200:
            return f"Error: {data['message']}"
        
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        city_name = data['name']
        
        return f"The weather in {city_name} is {weather_description} with a temperature of {temperature}°C."
    except Exception as e:
        return f"Error retrieving weather data: {str(e)}"

# Wikipedia API
def get_wiki_summary(query):
    WIKI_API_URL = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    try:
        response = requests.get(WIKI_API_URL)
        data = response.json()
        
        if 'extract' in data:
            return data['extract']
        else:
            return "No summary found for the given query."
    except Exception as e:
        return f"Error retrieving Wikipedia summary: {str(e)}"

# Movie API
MOVIES_API_KEY = os.getenv('MOVIES_API_KEY')
MOVIES_BASE_URL = 'https://api.themoviedb.org/3/search/movie'

def get_movie_info(movie_name):
    try:
        params = {
            'api_key': MOVIES_API_KEY,
            'query': movie_name
        }
        response = requests.get(MOVIES_BASE_URL, params=params)
        data = response.json()
        
        if data['results']:
            movie = data['results'][0]
            title = movie['title']
            overview = movie['overview']
            release_date = movie['release_date']
            return f"Title: {title}\nRelease Date: {release_date}\nOverview: {overview}"
        else:
            return "Movie not found."
    except Exception as e:
        return f"Error retrieving movie data: {str(e)}"

# News API
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
NEWS_BASE_URL = 'https://newsapi.org/v2/top-headlines'

def get_news(country='us'):
    try:
        params = {
            'apiKey': NEWS_API_KEY,
            'country': country
        }
        response = requests.get(NEWS_BASE_URL, params=params)
        data = response.json()
        
        if data['status'] != 'ok':
            return f"Error: {data['message']}"
        
        articles = data['articles']
        news = ""
        for i, article in enumerate(articles[:5], start=1):
            news += f"{i}. {article['title']}.\n"
        
        return news
    except Exception as e:
        return f"Error retrieving news: {str(e)}"

# Reminder
reminders = []

def add_reminder(reminder_text, delay):
    def reminder():
        time.sleep(delay)
        print(f"Reminder: {reminder_text}")
    
    t = threading.Thread(target=reminder)
    t.start()
    reminders.append((reminder_text, delay))

def list_reminders():
    return reminders

# Joke API
JOKE_API_URL = 'https://v2.jokeapi.dev/joke/Any'

def get_joke():
    try:
        response = requests.get(JOKE_API_URL)
        data = response.json()
        
        if data['type'] == 'single':
            return data['joke']
        elif data['type'] == 'twopart':
            return f"{data['setup']} ... {data['delivery']}"
    except Exception as e:
        return f"Error retrieving joke: {str(e)}"

# Currency Converter
EXCHANGE_RATE_API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')
EXCHANGE_RATE_BASE_URL = 'https://v6.exchangerate-api.com/v6'

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"{EXCHANGE_RATE_BASE_URL}/{EXCHANGE_RATE_API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()
        
        if data['result'] != 'success':
            return f"Error: {data['error-type']}"
        
        conversion_result = data['conversion_result']
        return f"{amount} {from_currency} is equal to {conversion_result} {to_currency}"
    except Exception as e:
        return f"Error retrieving conversion data: {str(e)}"

# Translation
translator = Translator()

def translate_text(text, dest_language):
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Error translating text: {str(e)}"

# Timer
def set_timer(seconds):
    time.sleep(seconds)
    return "Time's up!"

# Basic Math Operations
def calculate(expression):
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception as e:
        return f"Error calculating expression: {str(e)}"
