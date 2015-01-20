#!/usr/bin/python

import re

import binascii



def replace(match):

    nw = hex(int(match.group(2),16)+int('43',16))[-2:]

    return match.group(2)+match.group(3)+match.group(4)+nw+match.group(6)





def main():

    pattern = re.compile(r'(?=((\w{2})(\w{2}0C)(0202010302)(\w{2})(03)))')

    f = open('txt_dump')

    

    for line in f:

#        for match in re.finditer(pattern, line):

#            print(match.group(1),match.group(2),match.group(3),match.group(4),match.group(5),match.group(6), hex(int(match.group(2),16)+int('43',16)))

#            nw = hex(int(match.group(3),16)+int('43',16))[-2:]

        a = pattern.sub(replace, line)        



    with open("out", "wb") as of:

        of.write(binascii.unhexlify(a))







if __name__ == '__main__':

    main()
