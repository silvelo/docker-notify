import notify
import os
import settings

if __name__ == "__main__":
    notify_status = os.getenv("NOTIFY_STATUS")
    timeout = os.getenv("TIMEOUT")

    n = notify.Notify(notify_status, timeout)
    n.start()
