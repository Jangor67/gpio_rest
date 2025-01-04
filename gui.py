from flask import Flask, render_template, request, send_from_directory
import requests
import logging
import sys

log = logging.getLogger()
log.setLevel(logging.INFO)

app = Flask(__name__)


@app.route('/')
def index():
    context = requests.get('http://127.0.0.1:5000/gpio/state?pin=18')
    # log.critical("state:", context.json())
    return render_template('index.html', **context.json())

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/png')

@app.route('/send', methods=['POST'])
def send():
    pin = request.form['pin']
    state = request.form['state']
    try:
        res = requests.post('http://127.0.0.1:5000/gpio', json={'pin': int(pin), 'state': int(state)})
        return render_template('index.html', **res.json())
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

