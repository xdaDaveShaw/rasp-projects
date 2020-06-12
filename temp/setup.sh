#!/usr/bin/env bash

sudo pip3 install --upgrade setuptools
sudo pip3 install adafruit-io
sudo apt install rng-tools -y
curl https://get.pimoroni.com/bme680 > bme680
more bme680
bash bme680
rm bme680

