# hdd-temp
This is simple script, that allows you to turn off your server, when temperature of HDD is too high.
Also you will have Telegram message about this issue.

Bu default update time = 60 sec. You can change it in `hdd-temp.service`

You need to do this:
1. Rename `.env-template` to `.env`
2. Fill `.env` file with temperature, token chat id and message prefix
3. Copy files to `/opt/koshi8bit/hdd-temp/`
   * env
   * main.py
   * telegram_my.py
   * requirements.txt 
   * hdd-temp.service 
4. Run commands below:
   * `sudo pip3 install -r /opt/koshi8bit/hdd-temp/requirements.txt`
   * `sudo cp /opt/koshi8bit/hdd-temp/hdd-temp.service /etc/systemd/system`
   * `sudo systemctl daemon-reload`
   * `sudo systemctl enable hdd-temp.service`
   * `sudo systemctl start hdd-temp.service`
    
5. To check for status and errors you can use commands below:
   * `sudo systemctl status hdd-temp.service`
   * `journalctl -e -u hdd-temp.service` 
   * `sudo watch hddtemp /dev/sda /dev/sdb`
   * `sudo systemctl restart hdd-temp.service`
    
6. FIN!

7. To stop this service you need to exec this:
   * `sudo systemctl disable hdd-temp.service`
   * `sudo systemctl stop hdd-temp.service` 