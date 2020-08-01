import os
from bs4 import BeautifulSoup
import requests


BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN") // Enter your telegram bot token here


def telegram_bot_sendtext(bot_message, bot_chatID):
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)


def pricecheck(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,features="html.parser")
    found = False
    for button in soup.find_all('button'):
        if('buy now' in button.text.lower()):
            found = True

    if(found):
        for class_name in soup.find_all():
            if(class_name.text.startswith('₹')):
                price=int(''.join(class_name.text.split(','))[1:])
                if(price<=14999):
                    print("yes")
                    telegram_bot_sendtext(url, '337297420')
                break

url1 = "https://www.flipkart.com/redmi-note-9-pro-aurora-blue-128-gb/p/itma84d60532d415"
url2 = "https://www.flipkart.com/redmi-note-9-pro-interstellar-black-128-gb/p/itma84d60532d415"
url3 = "https://www.flipkart.com/redmi-note-9-pro-glacier-white-128-gb/p/itm47612dff3ea66"

pricecheck(url1)
pricecheck(url2)
pricecheck(url3)
