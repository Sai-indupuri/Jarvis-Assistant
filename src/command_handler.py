# src/command_handler.py

from utils import (
    get_weather, get_wiki_summary, get_movie_info, get_news,
    add_reminder, list_reminders, get_joke, convert_currency,
    translate_text, set_timer, calculate
)

def handle_command(doc):
    text = str(doc).lower()
    
    if "weather" in text:
        city = text.split("in")[-1].strip()
        return get_weather(city)
    
    elif "wikipedia" in text or "wiki" in text:
        query = text.replace("wikipedia", "").replace("wiki", "").strip()
        return get_wiki_summary(query)
    
    elif "movie" in text:
        movie_name = text.replace("movie", "").strip()
        return get_movie_info(movie_name)
    
    elif "news" in text:
        country = text.split("in")[-1].strip()
        return get_news(country)
    
    elif "reminder" in text:
        parts = text.split("in")
        reminder_text = parts[0].replace("reminder", "").strip()
        delay = int(parts[-1].strip().split()[0]) * 60
        add_reminder(reminder_text, delay)
        return f"Reminder set for {reminder_text}"
    
    elif "joke" in text:
        return get_joke()
    
    elif "convert" in text:
        parts = text.split()
        amount = float(parts[1])
        from_currency = parts[2]
        to_currency = parts[-1]
        return convert_currency(amount, from_currency, to_currency)
    
    elif "translate" in text:
        parts = text.split("to")
        text_to_translate = parts[0].replace("translate", "").strip()
        dest_language = parts[-1].strip()
        return translate_text(text_to_translate, dest_language)
    
    elif "timer" in text:
        seconds = int(text.split()[-1])
        return set_timer(seconds)
    
    elif "calculate" in text:
        expression = text.replace("calculate", "").strip()
        return calculate(expression)
    
    else:
        return "I'm sorry, I didn't understand that command."
