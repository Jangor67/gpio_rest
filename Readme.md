This python program aims to allow to control GPIO outputs using a rest interface

Initial setup suggested by ChatGPT ;-)

# Setup

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip3 install flask RPi.GPIO
```

# Run

```
python3 rest.py &
python3 gui.py &
```

# Test

Check and change the used ip number accordingly

```
curl -X GET "http://192.168.178.63:5000/gpio/status?pin=18"
curl -X POST -H "Content-Type: application/json" -d '{"pin": 18, "state": 1}' "http://192.168.178.63:5000/gpio"
{"pin":18,"state":1}
```

or open url to gui at [port 8000](http://192.168.178.63:8000)

# Run as a service

Create a service file
```
sudo nano /etc/systemd/system/gpio_rest.service
```

Add following content
```
[Unit]
Description=GPIO REST API
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/gpio_rest/rest.py
WorkingDirectory=/home/pi
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Startup
```
sudo systemctl enable gpio_rest
sudo systemctl start gpio_rest
```
