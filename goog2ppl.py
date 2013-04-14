#!/usr/bin/env python
# Python's regular expression library
import re
import sys

# Gets first command line argument
source = open(sys.argv[1])

outCard = []

cardNum = 0
for line in source:
    if not re.search(r'END:VCARD', line):
        outCard.append(line)
        if re.search(r'(N:)(.+)(;;;)', line):
            contact = re.sub(r'(N:)(.+)(;;;)', r'\2.vcf', line)
            contact = contact.replace(';','')
            if re.search(r'(N:)(;;;)', line):
                contact = 'MISSING CONTACT FIELD ' + str(cardNum) + contact
        fileName = open(contact, 'w')
    elif re.search(r'END:VCARD', line):
        outCard.append(line)
        for line in outCard:
            fileName.write("%s" % line)
        outCard = []
        cardNum = cardNum + 1
