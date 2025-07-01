from app import create_app  # Import the Flask app creation function
from app.voice_input import listen_to_user  # Voice input logic
from app.assistant import get_response      # Logic to handle voice commands
from app.tts_engine import speak            # Speak the response out loud

app = create_app()  # Initialize Flask app (we're not using it directly here, but ready for expansion)

if __name__ == "__main__":  # This block runs only when you directly run this file (not when imported)
    print("🎙️ Say something to the voice assistant...")  # User prompt

    while True:  # Infinite loop to keep listening
        try:
            user_input = listen_to_user()  # Record and convert voice to text
            print(f"You said: {user_input}")  # Show what the user said

            response = get_response(user_input)  # Get assistant's reply
            print(f"Assistant: {response}")  # Show the reply
            speak(response)  # Use TTS to speak the reply

        except Exception as e:
            print("Error:", str(e))  # Print any error that occurs
