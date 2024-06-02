# Jarvis - A Virtual Assistant

## Overview

Jarvis is a Python-based virtual assistant that recognizes spoken commands and performs various tasks such as fetching weather information, summarizing Wikipedia articles, and providing movie information.
## Features

- **Speech Recognition**: Recognizes and processes spoken commands.
- **Natural Language Processing**: Processes commands using spaCy.
- **Text-to-Speech**: Responds to commands with spoken responses.
- **Weather Information**: Fetches current weather information for a specified city.
- **Wikipedia Summary**: Provides summaries of Wikipedia articles.
- **Movie Information**: Retrieves movie information.
- **News Fetching**: Fetches and reads out the latest news headlines.
- **Reminder/To-Do List**: Sets reminders and manages a to-do list.
- **Jokes**: Fetches random jokes.
- **Currency Conversion**: Converts currency values.
- **Translation**: Translates text between languages.
- **Timer**: Sets a timer.
- **Basic Math Operations**: Performs basic math calculations.



## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sai-indupuri/Jarvis-Assistant.git
    cd Jarvis-Assistant
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Download spaCy Model**:
    ```bash
    python -m spacy download en_core_web_sm
    ```

6. **Set Up Environment Variables**:
    Create a `.env` file in the project root and add the following:
    ```env
    WEATHER_API_KEY=your_weather_api_key_here
    MOVIES_API_KEY=your_movies_api_key_here
    NEWS_API_KEY=your_news_api_key_here
    EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key_here
    ```

## Usage

 **Run the Main Program**:
    ```bash
    python src/main.py
    ```

## Contributing
Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.