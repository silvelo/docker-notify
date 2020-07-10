from slack_logger import SlackHandler
from telegram_handler import TelegramHandler

import os
import logging
import sys


class CustomLogger():

    def __init__(self, conf):
        self._brief_format = logging.Formatter('%(message)s')
        self._time_format = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger('docker_notify')
        self.conf = conf
        self.logger.setLevel(logging.DEBUG)
        self.get_slack_handler()
        self.get_telegram_handler()
        self.get_stream_hanlder()

    def get_slack_handler(self):
        slack_hook_url = self.conf.get('SLACK_HOOK_URL', None)
        if slack_hook_url:
            slack_handler = SlackHandler(url=slack_hook_url)
            slack_handler.setLevel(logging.INFO)
            slack_handler.setFormatter(self._brief_format)

            self.logger.addHandler(slack_handler)

    def get_telegram_handler(self):
        telgram_token = self.conf.get('TELGRAM_TOKEN', None)
        telegram_chat_id = self.conf.get('TELEGRAM_CHAT_ID', None)

        if telgram_token and telegram_chat_id:
            telegram_handler = TelegramHandler(
                token=telgram_token, chat_id=telegram_chat_id)
            telegram_handler.setFormatter(self._brief_format)
            telegram_handler.setLevel(logging.INFO)
            self.logger.addHandler(telegram_handler)

    def get_stream_hanlder(self):
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(self._time_format)
        stream_handler.setLevel(logging.DEBUG)
        self.logger.addHandler(stream_handler)
