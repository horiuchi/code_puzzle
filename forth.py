#!/usr/bin/python -w

import itertools
from second_code import Bars
from third_code import decode_morse

r="""
***************
ITT TI I T TIii
T i  I Iii  TTT
"""

table = {' ':[' ','T'],'i':['T',' '],'T':['i','I'],'I':['I','i']}
s = 'ITT TI I T TIii'

def inverse():
    pat = []
    for c in list(s):
        pat.append(table[c])

    for p in itertools.product(*pat):
        line = ''.join(p)
        bs = Bars(line)
        n = str(bs.next())
        if s == n:
            return line

print("answer: " + decode_morse(inverse()))

