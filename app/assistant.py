# Dictionary mapping voice inputs to responses
commands = {
    "hello": "Hello! How are you?",
    "what's your name": "I am your voice assistant.",
    "how are you": "I'm doing great. Thank you!",
    "what is the time": "Sorry, I can't tell time yet, but I will soon!",
    "open google": "I can't browse the web yet, but I can chat with you!",
    "tell me a joke": "Why did the developer go broke? Because he used up all his cache!",
    "what can you do": "I can answer simple questions for now.",
    "goodbye": "Goodbye! Have a nice day.",
    "thank you": "You're welcome!",
    "who created you": "I was created by a Python developer like you!",
}

def get_response(message):
    for key in commands:  # Loop through each command
        if key in message:  # If the key phrase is found in the message
            return commands[key]  # Return the corresponding response
    return "I don't understand that yet."  # Default if no match found
