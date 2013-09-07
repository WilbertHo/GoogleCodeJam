#!/usr/bin/python
import sys

class Translator(object):
    def __init__(self, languages=None):
        languages = languages or []

        # First line is number of test cases
        numCases = languages.pop(0)

    def translate(self):
        pass

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    languages = f.readlines()
    f.close()
    translator = Translator(languages)
