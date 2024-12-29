# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:26:58 2022

@author: ADMIN
"""

# Import necessary libraries
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import pywhatkit as pw  # To play YouTube videos
from datetime import date  # For date functionality
import datetime  # For time functionality
import wikipedia  # For fetching information from Wikipedia
import pyjokes  # For fetching jokes
import webbrowser  # To open websites
import os  # For system-level tasks
import random  # To add random functionalities
import time  # For sleep functions
import requests  # For API calls (e.g., to fetch news)

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice of the assistant
voices = engine.getProperty('voices')  # Fetch available voices
engine.setProperty('voice', voices[1].id)  # Use the second voice (can be changed as needed)

# Function to make the assistant talk
def talk(text):
    engine.say(text)  # Pass the text to be spoken
    engine.runAndWait()  # Ensure the speech is completed

# Function to take voice commands from the user
def take_command():
    try:
        with sr.Microphone() as source:  # Open microphone as input source
            print("Listening.....")  # Indicate that the assistant is listening
            voice = listener.listen(source)  # Listen to the input
            command = listener.recognize_google(voice)  # Recognize and convert speech to text
            command = command.lower()  # Convert command to lowercase for consistency
            if 'alexa' in command:  # Trigger word check
                command = command.replace('alexa', '')  # Remove 'alexa' from command
                print(command)  # Print the processed command
    except:
        pass  # Handle exceptions gracefully
    return command  # Return the recognized command

# Main function to run the assistant
def run_alexa():
    command = take_command()  # Fetch the user command
    print(command)  # Print the command for debugging
    
    # Respond to different commands
    if 'play' in command:  # Play a song or video on YouTube
        song = command.replace('play', '')  # Extract the song name
        talk('playing ' + song)  # Announce the action
        pw.playonyt(song)  # Use pywhatkit to play on YouTube

    elif 'time' in command:  # Tell the current time
        time = datetime.datetime.now().strftime('%I:%M %p')  # Format the time
        print(time)  # Print the time
        talk('Current time is ' + time)  # Announce the time

    elif 'date' in command:  # Tell the current date
        today = date.today()  # Get today's date
        print(today)  # Print the date
        talk('Today is ' + today.strftime('%B %d, %Y'))  # Announce the formatted date

    elif 'who is' in command:  # Fetch information about a person or topic
        person = command.replace('who is', '')  # Extract the query
        info = wikipedia.summary(person, 1)  # Get a summary from Wikipedia
        print(info)  # Print the information
        talk(info)  # Announce the information

    elif 'open youtube' in command:  # Open YouTube in the browser
        talk('Opening YouTube')  # Announce the action
        webbrowser.open('https://www.youtube.com')  # Open YouTube

    elif 'open google' in command:  # Open Google in the browser
        talk('Opening Google')  # Announce the action
        webbrowser.open('https://www.google.com')  # Open Google

    elif 'open stack overflow' in command:  # Open Stack Overflow
        talk('Opening Stack Overflow')  # Announce the action
        webbrowser.open('https://stackoverflow.com')  # Open Stack Overflow

    elif 'search for' in command:  # Perform a Google search
        search_query = command.replace('search for', '')  # Extract the query
        talk('Searching for ' + search_query)  # Announce the search
        webbrowser.open('https://www.google.com/search?q=' + search_query)  # Perform the search

    elif 'shutdown computer' in command:  # Shutdown the computer
        talk('Shutting down the computer')  # Announce the action
        os.system('shutdown /s /t 1')  # Execute shutdown command

    elif 'restart computer' in command:  # Restart the computer
        talk('Restarting the computer')  # Announce the action
        os.system('shutdown /r /t 1')  # Execute restart command

    elif 'joke' in command:  # Tell a joke
        joking = pyjokes.get_joke(language='en', category='all')  # Fetch a random joke
        print(joking)  # Print the joke
        talk(joking)  # Announce the joke

    elif 'weather' in command:  # Placeholder for weather-related functionality
        talk('Sorry, I am not equipped to provide weather updates yet.')

    elif 'are you single' in command:  # Respond to a personal question humorously
        talk('I am in a relationship with vaibhav')

    elif 'help' in command:  # Respond to a help request humorously
        talk('I am here to assist you with tasks. Try saying a command.')

    elif 'quote' in command:  # Provide a random inspirational quote
        quotes = [
            "The only way to do great work is to love what you do. – Steve Jobs",
            "Life is what happens when you're busy making other plans. – John Lennon",
            "In the middle of difficulty lies opportunity. – Albert Einstein",
            "It does not matter how slowly you go as long as you do not stop. – Confucius"
        ]
        quote = random.choice(quotes)  # Select a random quote
        talk(quote)  # Announce the quote

    elif 'news' in command:  # Fetch the latest news headlines (from an API or static list)
        try:
            response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY")
            data = response.json()
            articles = data["articles"]
            headlines = [article["title"] for article in articles[:5]]
            talk("Here are the latest headlines: " + ", ".join(headlines))
        except:
            talk("Sorry, I couldn't fetch the latest news right now.")

    elif 'calculate' in command:  # Perform simple arithmetic calculations
        try:
            command = command.replace('calculate', '')  # Remove 'calculate' keyword
            result = eval(command)  # Evaluate the expression
            talk(f"The result is {result}")  # Announce the result
        except:
            talk("Sorry, I couldn't process the calculation. Please try again.")

    elif 'tell me a fun fact' in command:  # Provide a random fun fact
        facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old!",
            "A group of flamingos is called a 'flamboyance'.",
            "Bananas are berries, but strawberries aren't!",
            "Cleopatra lived closer in time to the first Moon landing than to the building of the Great Pyramid."
        ]
        fact = random.choice(facts)  # Select a random fun fact
        talk(fact)  # Announce the fun fact

    else:  # Fallback for unknown commands
        talk('I did not understand that. Please say the command again.')

# Run the assistant in a continuous loop
while True:
    run_alexa()  # Keep the assistant running
