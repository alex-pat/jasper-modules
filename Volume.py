# -*- coding: utf-8-*-
import re
from os import system

WORDS = ["VOLUME", "SOUND"]


def handle(text, mic, profile):
    """
    Responds to user-input, typically speech text, with a summary of
    the relevant weather for the requested date (typically, weather
    information will not be available for days beyond tomorrow).

    Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    if "up" in text:
        action = '+'
    elif "down" in text:
        action = '-'
    system("amixer -D plughw:1,0 set PCM 30%" + action)
    mic.say("Ok, %", text)


def isValid(text):
    """
        Returns True if the text is related to the weather.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return any(word in text.upper() for word in WORDS)
