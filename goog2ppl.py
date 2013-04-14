#!/usr/bin/env python
# Python's regular expression library
import re
import sys

# Gets first command line argument
source = open(sys.argv[1])

outCard = []

cardNum = 0
for line in source:
    fileName = open('tempname' + str(cardNum) + '.vcf', 'w')
    if not re.search(r'END:VCARD', line):
        #outCard.append(line)
        if re.search(r'(N:)(.+)(;;;)', line)
        print line
    '''
    elif re.search(r'END:VCARD', line):
        outCard.append(line)
        for line in outCard:
            fileName.write("%s" % line)
        outCard = []
        cardNum = cardNum + 1
    '''
