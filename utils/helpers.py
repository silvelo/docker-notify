import argparse


class ParseArguments:

    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._define_arguments()
        self._args = self._parser.parse_args()

    def get_values(self):
        args_dict = self._args.__dict__

        filtered = {k: v for k, v in args_dict.items() if v is not None}

        return filtered

    def _define_arguments(self):
        self._parser.add_argument(
            "-k", "--notify_status", help="kafka ip server <ip:port>", type=str, required=True)
        self._parser.add_argument(
            "-c", "--consumer_topics", help="kafka consumer topic. Multiple values are available", type=str, required=True, action='append')
        self._parser.add_argument(
            "-p", "--producer_topic", help="kafka producer topic", type=str, required=True)
        self._parser.add_argument(
            "-g", "--group_id", help="kafka consumer group", type=str)
        self._parser.add_argument(
            "-tc", "--c_timeout", help="Consumer poll interval", type=int)
        self._parser.add_argument(
            "-tp", "--p_timeout", help="Producer poll interval", type=int)
        self._parser.add_argument(
            "-o", "--offset", help="Define reset offset", type=str)
