import os
import re
import datetime
import subprocess
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.storage import SQLStorageAdapter
import spacy
import nltk


# Explicitly set the NLTK data path
nltk.data.path.append('/home/miyato/nltk_data')

try:
    # Ensuring that the correct model is loaded
    nlp = spacy.load('en_core_web_sm')
    print("Spacy model loaded successfully.")
except OSError as e:
    print(f"Error loading Spacy model: {e}")
    exit(1)

# Initialize the ChatBot with SQL Storage Adapter
lexi_bot = ChatBot(
    "Lexi",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.db',  # You can change the path for a different database
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ]
)
trainer = ChatterBotCorpusTrainer(lexi_bot)

# Load existing training data
def load_corpus_files():
    script_dir = os.path.dirname(__file__)
    corpus_path = os.path.join(script_dir, 'chatterbot_corpus')
    
    for filename in os.listdir(corpus_path):
        if filename.endswith('.yaml'):
            with open(os.path.join(corpus_path, filename), 'r') as file:
                try:
                    data = yaml.safe_load(file)
                    if isinstance(data, dict) and 'conversations' in data:
                        trainer.train(data['conversations'])
                    else:
                        print(f"Skipping {filename}, data format is not valid.")
                except Exception as e:
                    print(f"Error loading {filename}: {e}")

load_corpus_files()  # Load initial training data

# Function to save user interactions
def save_user_interaction(user_input, bot_response):
    # Store the interaction directly in the database via ChatterBot
    lexi_bot.learn_response(bot_response, user_input)

# Function to set the female voice in Festival and modify pitch and rate
def set_voice(voice, rate=160, pitch=100):
    subprocess.call(['festival', '--batch', f"(set! voice_default '{voice})"])
    subprocess.call(['festival', '--batch', f"(Parameter.set 'Rate {rate})"])  # Set speaking rate
    subprocess.call(['festival', '--batch', f"(Parameter.set 'Pitch {pitch})"])  # Set pitch

# Function to speak text using Festival
def speak(text):
    process = subprocess.Popen(['festival', '--tts'], stdin=subprocess.PIPE, text=True)
    process.communicate(input=text)

# Set the voice properties (you can adjust the rate and pitch as needed)
set_voice('cmu_us_slt_cg', rate=180, pitch=120)  # Modify these values to your liking

# Function to greet the user based on the time of the day
def wish_user(user):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = f"Good Morning, {user}"
    elif 12 <= hour < 16:
        greeting = f"Good Afternoon, {user}"
    else:
        greeting = f"Good Evening, {user}"

    speak(greeting)
    print(greeting)

# Initial interaction with the user
speak("Hey there! What's your name, friend?")

# Get user's name
while True:
    user = input("Enter name: ")
    if re.search(r'[^\w\s]', user):
        print("Please do not enter any special characters.")
        speak("Please do not enter any special characters.")
        continue
    else:
        wish_user(user)
        speak(f"{user}, my name is LEXI, short for Linguistic Experience Interactive Bot. Let's chat.")
        break

# Start conversation
while True:
    query = input(f"{user}: ")
    response = lexi_bot.get_response(query)

    # Convert the response to a string
    response_text = str(response)

    print(f"Lexi: {response_text}")
    speak(response_text)  # Pass the string to the speak function

    # Save the interaction
    save_user_interaction(query, response_text)

    # Termination condition
    if query.lower() in ['exit', 'goodbye', 'bye']:
        break
