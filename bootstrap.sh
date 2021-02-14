#!/bin/bash

set -xue

sudo apt update
sudo apt install -y python3-dev python3-pip lm-sensors flameshot libiw-dev
sudo python3 -m pip install i3pystatus colour basiciw
sudo python3 -m pip install -IU git+https://github.com/enkore/i3pystatus.git
