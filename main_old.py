from dotenv import load_dotenv
from telegram_my import TelegramMy
import os, datetime
import subprocess

with open('/tmp/11111', 'w') as f:
    f.write('run ok')


if __name__ == '__main__':
    load_dotenv()
    teleg = TelegramMy(os.getenv('TELEGRAMTOKEN'), os.getenv('CHATID'))
    teleg.set_project_prefix('hdd-temp')

    # process = subprocess.Popen(["sudo hddtemp /dev/sda"], shell=False, stdout=subprocess.PIPE)
    # data = process.communicate()  # returns tuple
    # temp = int(data[0].split()[5][1:3])
    # # print(temp)
    # print(data[0])
    teleg.send('start ok')


