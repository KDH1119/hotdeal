from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import telegram
import asyncio
from hotdeal.models import Deal


response = requests.get('https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')

soup = BeautifulSoup(response.text, "html.parser")
BOT_TOKEN = '5845689361:AAEVmqD5VPctbePGLKap2vQz36ys2WQeETI'

bot = telegram.Bot(token=BOT_TOKEN)

async def test():

    row, _ = Deal.objects.filter(created_at__lte=datetime.now() -
    timedelta(days=7)).delete()
    print(row, "deals deleted")

    for item in soup.find_all("tr", {'class': ["list1", "list0"]}):
        try:
            image = item.find("img", class_="thumb_border").get("src")[2:]
            image = "http://" + image
            title = item.find("font", class_="list_title").text
            title = title.strip()
            link = item.find("font", class_="list_title").parent.get("href")
            link = "http://www.ppomppu.co.kr" + link
            reply_count = item.find("span", class_="list_comment2").text
            reply_count = int(reply_count)
            up_count = item.find_all("td")[-2].text
            up_count = up_count.split("-")[0]
            up_count = int(up_count)

            if '구글' in title and '기프트' in title:
                if (Deal.objects.filter(link__iexact=link).count() == 0):
                    Deal(image_url=image, title=title, link=link,
                         reply_count=reply_count, up_count=up_count).save()
                await bot.sendMessage(-1001897599228, '{} {}'.format(title, link))

        except Exception as e:
             continue

def run():
    asyncio.run(test())