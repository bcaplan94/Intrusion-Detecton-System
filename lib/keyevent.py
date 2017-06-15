#!/usr/bin/python3
"""
KeyEvent object

This is a data structure that stores a single key event and a timestamp for when the event happened.
It also has functionality to record an event.
As well as create a log of a two key event with the time between those events.
"""


class KeyEvent:
    key = None
    timestamp = None

    def record(self, key, timestamp):
        self.key = key
        self.timestamp = timestamp

    def log(self, key, timestamp):
        log_key = key + self.key
        log_value = self.timestamp - timestamp
        return {log_key: log_value}
