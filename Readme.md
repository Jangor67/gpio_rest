This python program aims to allow to control GPIO outputs using a rest 
interface.
It runs on a rather old Raspberry Pi B Rev 2.0 which is running Raspberry Pi OS 
or Raspbian 11 (Bullseye). *Note that 11 is outdated since it was released 
some time ago in 2021 and 12 (Bookworm) is already available since 2023.*

Initial setup and python code was suggested by ChatGPT ;-)

# Setup

```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip3 install flask RPi.GPIO
```

# Run

Run both python programs since one is supplying a rest interface and the other
one builds a gui on top of this rest interface.

```
python3 rest.py &
python3 gui.py &
```

# Test

You can test the rest interface first as well as the gui. *Be sure to 
check and change the used ip number accordingly.*

```
curl -X GET "http://192.168.178.63:5000/gpio/status?pin=18"
curl -X POST -H "Content-Type: application/json" -d '{"pin": 18, "state": 1}' "http://192.168.178.63:5000/gpio"
{"pin":18,"state":1}
```

open the gui using the following [url-to-the-gui](http://192.168.178.63:8000)

# Run as a service

Create a service file to run it automatically on startup should be done
like described below. *Note: This is not yet tested.*

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

Next Startup
```
sudo systemctl enable gpio_rest
sudo systemctl start gpio_rest
```
