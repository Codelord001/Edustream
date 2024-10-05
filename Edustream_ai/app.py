from flask import Flask, request, jsonify
from flask_cors import CORS
from Questgen import main

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

qg = main.QGen()

@app.get("/")
def welcomeHere():
    return "Welcome to this amazing question platform"

@app.post("/generate-mcq")
def generate_mcq():
    payload = request.json
    input_text = payload.get("input_text")
    print(input_text)
    if not input_text:       
        return jsonify({"error": "Invalid input, 'input_text' is required"}), 400

    # This line is redundant since input_text has been fetched earlier
    # input_text = payload.get("input_text") 

    short = qg.shortphrase({"input_text": input_text})

    print(short)
    return jsonify(short), 200

if __name__ == '__main__':  # Corrected line
    app.run(host='0.0.0.0', port=5000)
