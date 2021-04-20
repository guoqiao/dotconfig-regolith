#!/bin/bash

set -xue

# for regolith and default i3xrocks
sudo add-apt-repository --yes ppa:regolith-linux/release
sudo apt install -y regolith-desktop-standard i3xrocks

# for i3pystatus
sudo apt install -y python3-dev python3-pip lm-sensors flameshot libiw-dev
sudo python3 -m pip install -U pip
sudo python3 -m pip install -U pytz colour basiciw
sudo python3 -m pip install -I -e git+https://github.com/guoqiao/i3pystatus.git#egg=i3pystatus
