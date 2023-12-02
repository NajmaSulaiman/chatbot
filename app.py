from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

def load_responses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

# Load responses from the JSON file
responses = load_responses('responses.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']

    # Use the global responses variable
    bot_response = get_bot_response(user_input)

    return jsonify({'bot_response': bot_response})

def get_bot_response(user_input):
    # Make the comparison case-sensitive for Arabic text
    return responses.get(user_input, "المعذرة ما فهمتك")

if __name__ == '__main__':
    app.run(debug=True)
