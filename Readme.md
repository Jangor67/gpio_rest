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
python3 gpio_rest.py
```

# Test

```
curl -X GET "http://<raspberry_pi_ip>:5000/gpio/status?pin=18"
curl -X POST -H "Content-Type: application/json" -d '{"pin": 18, "state": 1}' "http://192.168.178.63:5000/gpio"
{"pin":18,"state":1}
```

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
ExecStart=/usr/bin/python3 /path/to/gpio_rest.py
WorkingDirectory=/path/to
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
