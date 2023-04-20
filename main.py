import requests
from  gpt_handle import OpenGptChat
from dotenv import load_dotenv
import os

load_dotenv()
def sendmessage(channel_name, text):
    key = os.getenv('TELEGRAM_BOT_KEY') 
    response = requests.get(f'https://api.telegram.org/bot{key}/sendMessage', {
        'chat_id': channel_name,
        'text': f'{text}'
    })
    return response

newsgpt = OpenGptChat().resumo()
print(sendmessage('@smartedge_news',newsgpt))