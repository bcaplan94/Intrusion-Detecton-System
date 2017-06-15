#!/usr/bin/python3
"""
Keylogger methods.
Used to get keyboard input.

Provides functionality for getting the key pressed and
getting the time since last key press
"""

import time


def key_log(event):
    """
    Run everytime a key event happens, right now just prints the character to the console
    :param event:
    :return:
    """

    return event.Key, time.time()
