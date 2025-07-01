# Voice Assistant - Python Terminal App

A simple voice assistant built in Python that listens to your voice commands in the terminal, responds with text and speaks the reply aloud using text-to-speech (TTS).  
This project uses Flask for potential future web integration and modular design with separate files for voice input, response logic, and speech output.

---

## Features

- **Voice input** via microphone using Google's Speech Recognition API
- **Predefined voice commands** mapped to text responses
- **Text-to-Speech** output with `pyttsx3` (offline)
- Modular and clean code structure for easy expansion
- Runs in terminal with continuous listening loop

---

## Demo

```bash
🎙️ Say something to the voice assistant...
Listening...
You said: hello
Assistant: Hello! How are you?
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/saugatpoudel100/voice_assistant.git
cd voice-assistant
Create and activate a virtual environment (recommended):

bash
Copy code
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the voice assistant with:

bash
Copy code
python run.py
Speak one of the supported commands, for example:

"hello"

"what's your name"

"tell me a joke"

"thank you"

"goodbye"

The assistant will respond accordingly with both text and voice.

Project Structure
bash
Copy code
voice_assistant/
│
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── assistant.py          # Command-response logic
│   ├── voice_input.py        # Microphone voice capture
│   └── tts_engine.py         # Text-to-speech engine
│
├── run.py                    # Main entry point script
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation
Dependencies
Python 3.7+

Flask 2.3.3

SpeechRecognition 3.10.1

pyttsx3 2.90

PyAudio 0.2.13

⚠️ If PyAudio installation fails on Windows, install it with pipwin:

bash
Copy code
pip install pipwin
pipwin install pyaudio
Extending the Assistant
Add more commands and responses in app/assistant.py

Integrate offline speech recognition (e.g., PocketSphinx)

Add wake word detection (e.g., "Hey Assistant")

Build a web or GUI interface using Flask or Tkinter

Use NLP models for smarter responses

License
MIT License © Your Name

Contact
Feel free to reach out via GitHub issues or email: your.email@example.com

yaml
Copy code

---

If you want, I can help you generate a **GitHub README badge**, or help you write instructions for **deployment or Dockerization** too!







Ask ChatGPT
