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
counter = 0
while True:
    if download(basestring + timestring + ".json.gz") is not None:
        asyncio.run(main())
        break
    else:
        counter += 1
        print(f"No Scrim Data yet. Ran for {counter} second{"s" if counter > 1 else ""}.")
    time.sleep(1)
