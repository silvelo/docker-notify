import os
import logging
import sys
from logging import StreamHandler
from slack_logger import SlackHandler
from telegram_handler import TelegramHandler


class CustomLogger():

    def __init__(self):
        self._log_format = logging.Formatter('%(message)s')
        self.logger = logging.getLogger(__name__)
        self.get_slack_handler()
        self.get_telegram_handler()
        self.get_stream_hanlder()

    def get_slack_handler(self):
        slack_hook_url = os.getenv('SLACK_HOOK_URL', None)
        if slack_hook_url:
            slack_handler = SlackHandler(url=slack_hook_url)
            slack_handler.setLevel(logging.INFO)
            slack_handler.setFormatter(self._log_format)
            self.logger.setLevel(logging.INFO)
            self.logger.addHandler(slack_handler)

    def get_telegram_handler(self):
        telgram_token = os.getenv('TELGRAM_TOKEN', None)
        telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID', None)

        if telgram_token and telegram_chat_id:
            telegram_handler = TelegramHandler(
                token=telgram_token, chat_id=telegram_chat_id)
            telegram_handler.setFormatter(self._log_format)
            telegram_handler.setLevel(logging.INFO)
            self.logger.addHandler(telegram_handler)

    def get_stream_hanlder(self):
        stream_handler = StreamHandler()
        stream_handler.setFormatter(self._log_format)
        stream_handler.setLevel(logging.INFO)
        self.logger.addHandler(stream_handler)
