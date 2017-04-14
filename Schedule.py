# -*- coding: utf-8-*-

WORDS = ["TASK"]

tasks = []

def handle(text, mic, profile):
    text = text.lower()
    if 'new' in text:
        mic.say('Ok, when?')
        date = mic.activeListen()
        mic.say('What task?')
        task = mic.activeListen()
        global tasks
        tasks.append([date, task])
        mic.say('OK, added %s at %s' % (task, date))
    elif 'next' in text:
        date, task = tasks[0]
        mic.say('Next task is %s at %s' % (task, date))
    elif 'all' in text:
        mic.say("Current tasks:")
        for date, task in tasks:
            mic.say('Task: %s at %s' % (task, date))
        mic.say("That's all")
    else:
        mic.say('Hmm... What?')

def isValid(text):
    return 'task' in text.lower()
