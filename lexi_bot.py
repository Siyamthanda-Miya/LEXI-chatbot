import pyttsx3
import re
import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from sqlalchemy import create_engine
import spacy


try:
    # Ensuring that the correct model is loaded
    nlp = spacy.load('en_core_web_sm')
    print("Spacy model loaded successfully.")
    # Returns an error message if the correct model is not loaded
except OSError as e:
    print(f"Error loading Spacy model: {e}")
    exit(1)

lexi_bot = ChatBot("Lexi", 
                   logic_adapters=[
            "chatterbot.logic.BestMatch",
            "chatterbot.logic.MathematicalEvaluation",
            "chatterbot.logic.TimeLogicAdapter"
            ])
trainer = ChatterBotCorpusTrainer(lexi_bot)
# accessing corpus training data
trainer.train("chatterbot.corpus.english")

# Initialize pyttsx3 engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)
voices_list = engine.getProperty('voices')
engine.setProperty('voice', voices_list[1].id)

# Function to greet the user based on the time of the day
def wish_user(user):
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        greeting = f"Good Morning, {user}"
    elif 12 <= hour < 16:
        greeting = f"Good Afternoon, {user}"
    else:
        greeting = f"Good Evening, {user}"

    engine.say(greeting)
    print(greeting)
    engine.runAndWait()

# Initial interaction with the user
engine.say("Hey there! What's your name, friend?")
engine.runAndWait()

# Get user's name
while True:
    user = input("Enter name: ")
    # checking if user input has special characters
    if re.search(r'[^\w\s]', user):
            print("Please do not enter any special characters.")
            engine.say("Please do not enter any special characters.")
            engine.runAndWait()
            continue
    else:
        wish_user(user)
        engine.say(f"{user}, my name is LEXI, short for Linguistic Experience Interactive Bot. Let's chat.")
        engine.runAndWait()
        break

# Start conversation
while True:
    query = input(f"{user}: ")
    response = lexi_bot.get_response(query)
    print(f"Lexi: {response}")
    engine.say(response)
    engine.runAndWait()

    # Termination condition
    if query.lower() == 'exit' or query == 'goodbye'.IS or query == 'bye':
        break
