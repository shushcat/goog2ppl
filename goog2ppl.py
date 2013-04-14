#!/usr/bin/env python
# Python's regular expression library
import re
import sys

# Gets first command line argument
source = open(sys.argv[1])

contact = ''
outCard = []

cardNum = 0
for line in source:
    if not re.search(r'END:VCARD', line):
        # Is it a N: line?
        if re.search(r'(N:)(.+)(;;;)', line):
            contact = (re.sub(r'(N:)(.+)(;;;)', r'\2', line)).replace(';','')
            if re.search(r'(N:)(;;;)', line):
                contact = 'MISSING CONTACT FIELD ' + str(cardNum)
            # Get rid of extra newlines.
            contact = contact.rstrip()
            line = (re.sub(r'(N:)(.+)(;;;)', r'\1%s\3' % contact, line))
    outCard.append(line)
    if re.search(r'END:VCARD', line):
        fileName = open(contact + '.vcf', 'w')
        for line in outCard:
            fileName.write("%s" % line)
        outCard = []
        cardNum = cardNum + 1
