sudo pip3 install -r /opt/koshi8bit/hdd-temp/requirements.txt
sudo chmod +x /opt/koshi8bit/hdd-temp/restart.sh

sudo cp /opt/koshi8bit/hdd-temp/hdd-temp.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable hdd-temp.service
sudo systemctl start hdd-temp.service
sudo systemctl status hdd-temp.service

sudo systemctl restart hdd-temp.service


journalctl -e -u hdd-temp.service
sudo systemctl disable hdd-temp.service
sudo systemctl stop hdd-temp.service