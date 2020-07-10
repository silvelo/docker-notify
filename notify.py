import time
import requests_unixsocket
import logging
import os

import sys


class Notify():
    def __init__(self, conf):
        self.conf = conf
        self.logger = logging.getLogger('docker_notify')

        self._sock_url = 'http+unix://%2Fvar%2Frun%2Fdocker.sock/containers/json?all=1'
        secret_conf = {**conf, **{
            'TELGRAM_TOKEN': '*',
            'SLACK_HOOK_URL': '*',
            'TELEGRAM_CHAT_ID': '*'
        }}
        self.logger.debug(
            'Start docker notify with conf: {}'.format(secret_conf))

    def start(self):
        self.logger.debug('Start Docker Notify ')

        while True:

            message = ""
            containers = self._create_session()

            for container in containers:
                container_name = container['Names'][-1]
                container_state = container['State']
                if container_state in self.conf.get('NOTIFY_STATUS'):
                    message = "{}\nName: {}\nState: {}".format(
                        message, container_name, container_state)

            self.logger.info(message)
            self.logger.debug('Sleep until next check')
            time.sleep(self.conf.get('TIME_OUT'))

    def _create_session(self):
        session = requests_unixsocket.Session()
        r = session.get(self._sock_url)
        return r.json()
