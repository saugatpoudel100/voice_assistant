import pyttsx3  # Import the text-to-speech library

engine = pyttsx3.init()  # Initialize the TTS engine

# Set voice properties
engine.setProperty('rate', 150)  # Set speaking speed
engine.setProperty('volume', 1)  # Set volume (1 is max)

def speak(text):
    engine.say(text)  # Queue the text to be spoken
    engine.runAndWait()  # Process the queued text and speak
