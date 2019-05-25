#!/bin/bash

# Get OS dependencies.
sudo apt-get install python3 python3-pip mysql-server default-libmysqlclient-dev

# Get Python 3 dependencies.
pip3 install adafruit-circuitpython-bme280 django bootstrap4 mysqlclient

# Setup database.
sudo mysql -u root < setup.sql

# Add something like this to /etc/rc.local to run collect_data.py on boot.
# /home/pi/workspace/local-climate-detail/collect_data.py >> /home/pi/workspace/collect_data.log 2>&1 &

which python3
