import time
import requests_unixsocket
import logging
import os
from custom_logging import CustomLogger


class Notify:
    def __init__(self, notify_status=[], timeout=0):
        self.logger = CustomLogger().logger
        self.notify_status = notify_status
        self.timeout = timeout
        self._sock_url = 'http+unix://%2Fvar%2Frun%2Fdocker.sock/containers/json?all=1'

    def start(self):
        while True:
            try:
                containers = self._create_session()

                for container in containers:
                    container_name = container['Names'][-1]
                    container_state = container['State']
                    if container_state in self.notify_status:
                        self.logger.info("Name: {}\nState: {}".format(
                            container_name, container_state))
                time.sleep(int(self.timeout))
            except Exception as e:
                self.logger.error(e, exc_info=True)

    def _create_session(self):

        session = requests_unixsocket.Session()
        r = session.get(self._sock_url)
        return r.json()
