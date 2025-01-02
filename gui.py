from flask import Flask, render_template, request, send_from_directory
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/png')

@app.route('/send', methods=['POST'])
def send():
    pin = request.form['pin']
    state = request.form['state']
    try:
        res = requests.post('http://192.168.178.63:5000/gpio', json={'pin': int(pin), 'state': int(state)})
        return f"Response: {res.json()}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

