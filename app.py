from flask import Flask
# from flask_cors import CORS
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)
# CORS(app)

from routes import *

if __name__ == "__main__":
    app.run(port=5002)