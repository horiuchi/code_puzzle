#!/usr/bin/python -w


def decode_morse(s):
    result = []
    for x in s.split(' '):
        result.append(_morse(x))
    return ''.join(result)

def _morse(s):
    table = {'iI':'a','Iiii':'b','IiIi':'c','Iii':'d','i':'e',
             'iiIi':'f','IIi':'g','iiii':'h','ii':'i','iIII':'j',
             'IiI':'k','iIii':'l','II':'m','Ii':'n','III':'o',
             'iIIi':'p','IIiI':'q','iIi':'r','iii':'s','I':'t',
             'iiI':'u','iiiI':'v','iII':'w','IiiI':'x','IiII':'y','IIii':'z'}
    try:
        return table[s]
    except KeyError:
        return ''


