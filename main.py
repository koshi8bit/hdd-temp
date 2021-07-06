import datetime
import os
import subprocess

from dotenv import load_dotenv

from telegram_my import TelegramMy

with open('/tmp/11111', 'a') as f:
    now = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    f.write(f'{now}\n')

if __name__ == '__main__':
    load_dotenv()
    telega = TelegramMy(os.getenv('TELEGRAMTOKEN'), os.getenv('CHATID'))
    telega.set_project_prefix('k8b001@hdd-temp')
    telega.send('k8b001 startup ok')

    bashCmd = ["hddtemp", "/dev/sda"]
    process = subprocess.Popen(bashCmd, shell=False, stdout=subprocess.PIPE)
    output, error = process.communicate()  # returns tuple
    # temp = int(data[0].split()[5][1:3])
    # # print(temp)
    # print(data[0])

    telega.send(str(output))



