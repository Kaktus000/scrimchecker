import asyncio
import datetime
import time
import requests

def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None

from desktop_notifier import DesktopNotifier
basestring = "https://hiddengems.gymnasiumsteglitz.de/dl/stats/"
timestring = datetime.datetime.now().strftime("%Y-%m-%d")
notifier = DesktopNotifier()

async def main():
    await notifier.send(title="Scrims Released!", message="Hidden Gems Update")
while True:
    if download(basestring + timestring + ".json.gz") is not None:
        asyncio.run(main())
        break
    else:
        print("No Scrim Data yet")
    time.sleep(1)
