pip3 install -r /opt/koshi8bit/hdd-temp/requirements.txt

journalctl -e -u hdd-temp.service

sudo cp /opt/koshi8bit/hdd-temp/hdd-temp.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable hdd-temp.service
sudo systemctl start hdd-temp.service
sudo systemctl status hdd-temp.service

sudo systemctl disable hdd-temp.service