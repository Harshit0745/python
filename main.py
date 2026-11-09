import time
from plyer import notification


def water_reminder():
    while True:
        notification.notify(
            title="hello",
            message="this is a player notification!",
            timeout=10
            )
        time.sleep(3600)

            

