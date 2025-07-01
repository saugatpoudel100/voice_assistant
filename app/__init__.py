from flask import Flask  # Import Flask class

def create_app():
    app = Flask(__name__)  # Create a Flask app instance
    return app  # Return the app object
