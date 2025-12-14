from flask import Flask, render_template, request, jsonify
import rules

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    mode = data.get('mode', 'academic')
    
    response = rules.get_response(user_message, mode)
    return jsonify({'response': response, 'mode': mode})

if __name__ == '__main__':
    app.run(debug=True)