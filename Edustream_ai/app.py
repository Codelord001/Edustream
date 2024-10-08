from flask import Flask, request, jsonify
from flask_cors import CORS
from .Questgen import main

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

qg = main.QGen()

@app.route("/")
def welcome_here():
    return "Welcome to this amazing question platform"

@app.route("/generate-mcq", methods=['POST'])
def generate_mcq():
    payload = request.json
    input_text = payload.get("input_text")
    
    if not input_text:       
        return jsonify({"error": "Invalid input, 'input_text' is required"}), 400

    try:
        short = qg.shortphrase({"input_text": input_text})
        return jsonify(short), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# For debugging purposes, you can uncomment these lines
# print("Python path:", sys.path)
# print("Current working directory:", os.getcwd())
# print("Contents of current directory:", os.listdir())
# print("Contents of Edustream_ai directory:", os.listdir('Edustream_ai'))