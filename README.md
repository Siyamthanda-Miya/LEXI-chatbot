# Lexi - Linguistic Experience Interactive Bot

Lexi is an interactive chatbot that uses natural language processing (NLP) and text-to-speech (TTS) to engage in conversations with users. Lexi is built using Python, with the help of libraries such as `ChatterBot`, `Spacy`, and `pyttsx3`.

## Features
- **Text-to-Speech (TTS):** Lexi uses the `pyttsx3` library to convert text responses to speech, making the interaction more engaging.
- **Natural Language Processing (NLP):** Lexi utilizes the `Spacy` library to process text input and generate responses.
- **Conversational Logic:** Lexi is powered by `ChatterBot`, which is trained on the English language corpus to provide intelligent responses.
- **Time-Based Greeting:** Lexi greets the user based on the current time of day.

## Installation

To set up the project, you'll need to install the necessary Python libraries. You can do this by running the following commands:

```bash
pip install pyttsx3
pip install chatterbot==1.0.4
pip install chatterbot_corpus==1.2.0
pip install spacy==2.3.5
pip install sqlalchemy==1.2.19
pip install en_core_web_sm==2.3.1
```

## Usage

1. **Run the Script:**
   Start the chatbot by running the Python script:

   ```bash
   python lexi_bot.py
   ```

2. **Interaction:**
   - Lexi will ask for your name. Enter your name without any special characters.
   - Lexi will greet you based on the current time of day.
   - You can then engage in a conversation with Lexi by typing your queries. Lexi will respond using text and speech.
   - To exit the conversation, type `exit`, `goodbye`, or `bye`.

3. **Example Conversation:**
   ```plaintext
   Lexi: Hey there! What's your name, friend?
   Enter name: John
   Lexi: Good Evening, John
   John: How are you?
   Lexi: I am good, thank you for asking!
   John: exit
   Lexi: Goodbye! Have a great day.
   ```

## Project Structure

```plaintext
lexi_bot.py        # Main Python script containing the chatbot logic
README.md          # Project documentation
```

## Dependencies

This project requires the following Python libraries:

- **pyttsx3:** A text-to-speech conversion library in Python.
- **ChatterBot:** A machine learning, conversational dialog engine.
- **ChatterBot Corpus:** Pre-trained language datasets for ChatterBot.
- **Spacy:** An NLP library for advanced text processing.
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Customization

- **Logic Adapters:** You can customize Lexi's responses by adding more `ChatterBot` logic adapters in the `lexi_bot.py` script.
- **Training Data:** Enhance Lexi's conversational abilities by training the bot with additional data or custom datasets.
- **Voice Settings:** Modify the TTS engine properties such as `rate` and `voice` to change the speed and voice of Lexi's responses.

## Troubleshooting

- **Spacy Model Error:** If you encounter an error loading the Spacy model, ensure that the `en_core_web_sm` model is properly installed using the command:

  ```bash
  python -m spacy download en_core_web_sm
  ```

- **No Speech Output:** If Lexi does not speak, verify that `pyttsx3` is installed correctly and the appropriate voice engine is set.

## Future Improvements

- **Enhanced Logic Adapters:** Implement more sophisticated logic adapters for better conversational flow.
- **Custom Responses:** Add personalized responses based on user data.
- **Voice Recognition:** Integrate voice input for a fully hands-free experience.

## License

This project is licensed under the MIT License.

---
