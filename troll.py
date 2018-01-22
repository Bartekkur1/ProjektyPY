from win32api import keybd_event
import time
import random


Base = {
    'ENTER': 13 }

def KeyUp(Key):
    keybd_event(Key, 0, 2, 0)


def KeyDown(Key):
    keybd_event(Key, 0, 1, 0)


def Press(Key, speed=1):
    rest_time = 0.05/speed
    if Key in Base:
        Key = Base[Key]
        KeyDown(Key)
        time.sleep(rest_time)
        KeyUp(Key)
        return True
    return False

def Write(Str, speed = 1):
    for s in Str:
        Press(s, speed)
        time.sleep((0.1 + random.random()/10.0) / float(speed))

input('Press ENTER to proceed')

while(True):
    Press('ENTER', 1)
    time.sleep(1)











