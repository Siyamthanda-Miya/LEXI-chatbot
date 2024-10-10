

README.md

```markdown
# Lexi - Linguistic Experience Interactive Bot

Lexi is an interactive chatbot built with Python 3.8 using `ChatterBot`, `Spacy`, and `Festival` for natural language processing and text-to-speech. It engages users in conversation and provides time-based greetings. The project can be run locally and is easily customizable with additional logic adapters or training data. Python 3.8 is recommended for optimal compatibility with `ChatterBot`.

##Features
- **Text-to-Speech (TTS):** Lexi uses the `Festival` library to convert text responses to speech, making the interaction more engaging.
- **Natural Language Processing (NLP):** Lexi utilizes the `Spacy` library to process text input and generate responses.
- **Conversational Logic:** Lexi is powered by `ChatterBot`, which is trained on the English language corpus to provide intelligent responses.
- **Time-Based Greeting:** Lexi greets the user based on the current time of day.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or greater
- pip (Python package installer)
- (Any other prerequisites, like specific OS requirements)

## Installation

Follow these steps to set up the project:
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/Siyamthanda-Miya/LEXI-chatbot
   cd LEXI-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Download the spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. Install Festival:
   - **For Windows:**
     - **Using Cygwin:**
       1. Install [Cygwin](https://www.cygwin.com/).
       2. Use the Cygwin terminal to install Festival:
          ```bash
          apt-cyg install festival
          ```
     - **Using Windows Subsystem for Linux (WSL):**
       1. Install a Linux distribution from the Microsoft Store (e.g., Ubuntu).
       2. Open the WSL terminal and install Festival:
          ```bash
          sudo apt-get update
          sudo apt-get install festival
          ```
     - **Precompiled Binaries:** Search for precompiled binaries of Festival for Windows online, but be cautious about the source.

   - **For Linux:**
     ```bash
     sudo apt-get install festival
     ```

   - **For macOS:**
     ```bash
     brew install festival
     ```

   - **Alternative TTS Engines:** If you prefer to use an alternative TTS engine, consider installing `gTTS` as it has native support for Windows.

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

- **Festival:** A text-to-speech conversion library.
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

- If you still encounter an error loading the Spacy model, run the following command:

  ```bash
  py -m pip install spacy==2.3.5 --only-binary :all:
  ```

- If you encounter an error installing any of the dependencies, run the following command:

  ```bash
  py -m pip install --upgrade pip setuptools wheel
  ```

- **No Speech Output:** If Lexi does not speak, verify that `Festival` is installed correctly and the appropriate voice engine is set.

## Future Improvements

- **Enhanced Logic Adapters:** Implement more sophisticated logic adapters for better conversational flow.
- **Custom Responses:** Add personalized responses based on user data.
- **Voice Recognition:** Integrate voice input for a fully hands-free experience.

## License

This project is licensed under the MIT License.

---
