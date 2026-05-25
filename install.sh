#!/bin/bash

echo "[*] Downloading and Installing FORGR..."

sudo mkdir -p /opt/forgr

# repository URLs 
sudo curl -sL https://raw.githubusercontent.com/venz-x/forgr-file_organizer/refs/heads/main/main.py -o /opt/forgr/main.py
sudo curl -sL https://raw.githubusercontent.com/venz-x/forgr-file_organizer/refs/heads/main/engine.py -o /opt/forgr/engine.py
sudo curl -sL https://raw.githubusercontent.com/venz-x/forgr-file_organizer/refs/heads/main/extension.py -o /opt/forgr/extensions.py

# Permission
sudo chmod +x /opt/forgr/main.py

# remove previous file link
sudo rm -f /usr/local/bin/forgr

# create syslink
sudo ln -s /opt/forgr/main.py /usr/local/bin/forgr

echo "[+] Install Complete! Type 'forgr' anywhere to begin."