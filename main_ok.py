from dotenv import load_dotenv
from telegram_my import TelegramMy
import os, datetime

with open('/tmp/11111', 'a') as f:
    now = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    f.write(f'{now}\n')
