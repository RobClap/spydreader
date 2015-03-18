#!/usr/bin/env python
import time
import argparse
import fileinput
import sys

parser = argparse.ArgumentParser(usage='Pipe a textfile in this script and it will spritz-like show it to you',description='Command-line speedreader')
parser.add_argument('--wpm', help='Words per minute', default='600')
args = parser.parse_args()
wpm=vars(args)["wpm"]

class constants:
    LINESIZE = 40
    VOWELS = ["a","e","i","o","u"]

class bcolors:
    BLUE = '\033[94m'
    RED = '\033[01;31m'
    ENDCOLOR = '\033[0m'

def splitter(word):
    toreturn = dict()
    if len(word) <=1:
        toreturn["prefix"]= ""
        toreturn["suffix"]= ""
        toreturn["pivot"] = word
        return toreturn
    else:
        found= False
        half = (len(word)) // 2 
        for i in range (half, 0,-1):
            if word[i].lower() in constants.VOWELS:
                found = True
                toreturn["prefix"]= word[0:i]
                toreturn["suffix"]= word[i + 1 : len(word)]
                toreturn["pivot"] = word[i]
        if not found:
            toreturn["prefix"]= word[0:half]
            toreturn["suffix"]= word[half + 1 : len(word)]
            toreturn["pivot"] = word[half]
    return toreturn

def wordprinter(data):
        towrite="\r" + " "*(constants.LINESIZE // 2 - len(data["prefix"])) + data["prefix"] + bcolors.RED + data["pivot"] + bcolors.ENDCOLOR + data["suffix"] + " "*(constants.LINESIZE // 2 - len(data["suffix"]))
        sys.stdout.write(towrite.encode('utf-8'))
        sys.stdout.flush() 


print ""  
print " "*(constants.LINESIZE //2 - 13)+u"-- Welcome to spydreader --"
print "-"*(constants.LINESIZE)
#print " "*(constants.LINESIZE//2) + "|"   
print ""

for line in sys.stdin:
    line = line.decode('utf-8')
    for word in line.split():
        data=splitter(word)
        wordprinter(data)
        time.sleep(60 / float(wpm))


print ""  
print ""  
print "-"*(constants.LINESIZE)
print " "*(constants.LINESIZE //2 - 4)+u"-- EOF --"
print ""
