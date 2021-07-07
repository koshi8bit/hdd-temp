import datetime
import os
import subprocess
import re
import traceback
import time

from dotenv import load_dotenv
from telegram_my import TelegramMy


# with open('/tmp/11111', 'a') as f:
#     now = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
#     f.write(f'{now}\n')


def get_temp(device, regex):
    bash_cmd = ["hddtemp", device]
    process = subprocess.Popen(bash_cmd, shell=False, stdout=subprocess.PIPE)
    output, error = process.communicate()  # returns tuple

    text = output.decode('utf-8')
    result = re.findall(regex, text)
    return int(result[0])


def check_temp(device, regex):
    temp = get_temp('/dev/sda', rregex)
    if temp > max_temp:
        send_and_shutdown(f'Temperature of {device} is too big ({temp}°C)')
    # else:
    #     telega.send(f'Temperature of {device} is OK ({temp}°C)')


def send_and_shutdown(text):
    delay_sec = 180
    telega.send(text, False)
    telega.send(f'*Shutting down in {str(delay_sec)} sec*', False)
    time.sleep(delay_sec)
    telega.send(f'*Shutting down..*', False)
    time.sleep(3)
    os.system('init 0')


if __name__ == '__main__':
    load_dotenv()
    max_temp = int(os.getenv('MAX_TEMP'))
    telega = TelegramMy(os.getenv('TELEGRAM_TOKEN'), os.getenv('TELEGRAM_CHAT_ID'))
    telega.set_project_prefix(os.getenv('TELEGRAM_PREFIX'))
    telega.send(f'startup ok. Max temp = {max_temp} {type(max_temp)}')

    try:
        rregex = r'(\d+)°C'
        check_temp('/dev/sda', rregex)
        check_temp('/dev/sdb', rregex)

    except Exception as ex:
        telega.send_text_as_file(traceback.format_exc(), None, False)
        send_and_shutdown(f'ERROR Exception: {str(ex)}')
        raise ex




