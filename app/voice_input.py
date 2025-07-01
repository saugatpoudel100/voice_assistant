import speech_recognition as sr  # Import the SpeechRecognition library

def listen_to_user():
    recognizer = sr.Recognizer()  # Create a recognizer object

    with sr.Microphone() as source:  # Use your microphone as input
        print("Listening...")  # Show listening status
        audio = recognizer.listen(source)  # Record the audio from the mic

    try:
        # Try converting the recorded audio to text using Google's free service
        text = recognizer.recognize_google(audio)
        return text.lower()  # Convert to lowercase for easy matching

    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."  # If speech is not clear

    except sr.RequestError:
        return "API unavailable."  # If there's a network issue or Google fails
