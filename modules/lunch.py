#!/usr/bin/env python
"""
lunch.py - Phenny lunch selection module
By Ori Rawlings
"""
import random
import os

default = "Jimmy John's"

def choose_lunch(phenny, input):
    choice = str(random.choice(load_lunches(phenny)))
    phenny.say(' '.join(('Why not eat at',choice,'for lunch today?')))
choose_lunch.commands = ['food', 'lunch']

def ensure(path):
    if os.path.isfile(path):
        return True
    print path, 'does not exist as file'
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        try:
            print 'Creating directory:', d
            os.makedirs(d)
        except OSError as e:
            print e
            return False
    print 'Opening', path, 'for writing'
    try:
        f = open(path, 'w+')
    except IOError as e:
        print e
        return False
    try:
        f.write(default)
    except IOError as e:
        print e
        return False
    finally:
        f.close()
    return True

def load_lunches(phenny):
    p = os.path.join(os.path.expanduser('~/.phenny'),'lunch','lunches.txt')
    if ensure(p):
        return [l.strip() for l in open(p)]
    else:
        print 'Could not find or create', path
        return [default]

if __name__ == '__main_': 
   print __doc__.strip()
