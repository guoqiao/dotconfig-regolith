#!/bin/bash

set -xue

sudo apt update
sudo apt install -y python3-dev python3-pip lm-sensors flameshot
sudo python3 -m pip install i3pystatus
