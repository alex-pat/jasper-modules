# -*- coding: utf-8-*-

import modules.Weather as weather
import modules.News as news
import modules.Time as time

WORDS = ["MORNING"]


def handle(text, mic, profile):
    mic.say("Good morning, %s" % profile['first_name'])
    time.handle('time', mic, profile)
    weather.handle('weather today', mic, profile)
    news.handle('news', mic, profile)
    mic.say("Have a nice day!")

def isValid(text):
    return 'good morning' in text.lower()
