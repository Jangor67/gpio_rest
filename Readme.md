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

Create the service files to run automatically on startup.
*Note: you can also use the nano editor if vi is not your favorite one :-)*

```
sudo vi /etc/systemd/system/gpio_rest.service
```

Add following content

```
[Unit]
Description=GPIO REST API
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/gpio-rest/rest.py
WorkingDirectory=/home/pi/gpio-rest
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

```
sudo vi /etc/systemd/system/gpio_gui.service
```

Add following content

```
[Unit]
Description=GPIO GUI
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/gpio-rest/gui.py
WorkingDirectory=/home/pi/gpio-rest
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

Next Enable and Startup these services

```
sudo systemctl enable gpio_rest
sudo systemctl enable gpio_gui
sudo systemctl start gpio_rest
sudo systemctl start gpio_gui
```

Following are some checks and usefull system commands

```
systemctl status
systemctl list-units --state=failed

journalctl -fu gpio_gui.service

sudo systemctl daemon-reload

sudo systemctl start gpio_rest
sudo systemctl start gpio_gui
```
