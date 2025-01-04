from flask import Flask, jsonify, request
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)  # Gebruik GPIO 18 als voorbeeld

# Flask app
app = Flask(__name__)

@app.route('/gpio', methods=['POST'])
def control_gpio():
    data = request.get_json()
    pin = data.get('pin')
    state = data.get('state')

    if pin is None or state is None:
        return jsonify({'error': 'Pin and state must be provided'}), 400

    try:
        pin = int(pin)
        state = int(state)
        GPIO.setup(pin, GPIO.OUT)  # Stel de pin in
        GPIO.output(pin, state)   # Zet de state
        return jsonify({'pin': pin, 'state': state}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/gpio/state', methods=['GET'])
def gpio_state():
    pin = request.args.get('pin')
    if pin is None:
        return jsonify({'error': 'Pin must be provided'}), 400

    try:
        pin = int(pin)
        # GPIO.setup(pin, GPIO.IN)  # Zet de pin als input om state te lezen
        state = GPIO.input(pin)
        return jsonify({'pin': pin, 'state': state}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()  # Zorg ervoor dat GPIO netjes wordt afgesloten

