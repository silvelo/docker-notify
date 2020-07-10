import os
import logging
import custom_logging
import notify


def get_config():
    return {
        'TELGRAM_TOKEN': os.getenv('TELGRAM_TOKEN', None),
        'SLACK_HOOK_URL': os.getenv('SLACK_HOOK_URL', None),
        'TELEGRAM_CHAT_ID': os.getenv('TELEGRAM_CHAT_ID', None),
        'TIME_OUT': int(os.getenv('TIME_OUT', "10")),
        'NOTIFY_STATUS': os.getenv(
            'NOTIFY_STATUS', '').split(',')
    }


if __name__ == "__main__":
    conf = get_config()

    custom_logging.CustomLogger(conf)

    n = notify.Notify(conf)
    n.start()
