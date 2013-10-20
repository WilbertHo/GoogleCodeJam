#!/usr/bin/python
import argparse
import sys


class Translator(object):
    """ Args:
            languages: string containing source number, source language
                       and target language
    """
    def __init__(self, languages=None):
        self.languages = languages or []

        # split the input into source number, source and target language
        self.sourceNum, self.sourceLang, self.targetLang = self.languages.split()
        self.sourceRadix = len(self.sourceLang)
        self.targetRadix = len(self.targetLang)

    def __str__(self):
        print "{src} {srcL} {tgtL}".format(src=self.sourceNum,
                                           srcL=self.sourceLang,
                                           tgtL=self.targetLang)

    def __repr__(self):
        print "{cls}({params})".format(cls=self.__class__.__name__,
                                       params=self.languages)

    def sourceValue(self):
        """ Get the value of source number """
        sourceNum = self.sourceNum
        sourceLang = self.sourceLang
        sourceRadix = self.sourceRadix

        # translate source number into an actual value
        num = 0
        # reverse so we can easily multiply easily
        for mult, digit in enumerate(sourceNum[::-1]):
            # Ex: 19 (0123456789) is 9 * 10^0 + 1 * 10^1
            num += sourceLang.index(digit) * (sourceRadix ** mult)

        # translate to the target language

        return num

    def translate(self):
        """ Translate the source number into the target language """
        sourceValue = self.sourceValue()
        targetLang = self.targetLang
        radix = self.targetRadix
        targetNum = []

        # Divide by the target radix and keep the remainder
        num = sourceValue

        while(num > 0):
            # Get the remainder of dividing number by radix
            # Ex: 9 in oF8 (radix: 3) should be Foo
            # 9 % 3 == 0, 9/3 == 3 -> 3 % 3 == 0, 3/3 == 1 -> 1 % 3 == 1
            targetNum.append(targetLang[num % radix])

            # Move to the next digit
            num = num / radix

        # Since we constructed the target number starting from the smallest
        # digit, reverse before returning
        return ''.join(targetNum[::-1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', dest='file', help='Input file')
    pargs = parser.parse_args()

    if not pargs.file:
        print 'Specify an input file'
        sys.exit()

    with open(pargs.file, 'r') as f:
        languages = [line.rstrip() for line in f.readlines()]

    # First line is number of test cases
    numCases = languages.pop(0)

    for caseNum, language in enumerate(languages, 1):
        print "Case #{caseNum}: {lang}".format(
            caseNum=caseNum,
            lang=Translator(language).translate())

if __name__ == '__main__':
    main()
