import asyncio
import datetime
import time
import requests
from desktop_notifier import DesktopNotifier

def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None

basestring = "https://hiddengems.gymnasiumsteglitz.de/dl/stats/"
timestring = datetime.datetime.now().strftime("%Y-%m-%d")
notifier = DesktopNotifier()

async def main():
    await notifier.send(title="Scrims Released!", message="Hidden Gems Update")

start_time = datetime.datetime.now()

while True:
    if download(basestring + timestring + ".json.gz") is not None:
        asyncio.run(main())
        break
    else:
        elapsed = datetime.datetime.now() - start_time
        formatted = str(elapsed).split(".")[0]
        print(f"No Scrim Data yet. Running for {formatted}.")
    time.sleep(60)
