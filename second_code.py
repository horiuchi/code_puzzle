#!/usr/bin/python -w


class SimpleBars(list):

    def __init__(self, s):
        list.__init__(self, s)

    def __str__(self):
        return "".join(self)

    def _next(self, l, i):
        x = l[i]
        xp = l[i-1]
        xn = l[(i+1) % len(l)]
        if x == ' ':
            if xp == 'i' and xn == 'i':
                return ' '
            elif xp == 'i' or xn == 'i':
                return 'i'
            else:
                return ' '
        elif x == 'T':
            if xp == 'i' and xn == 'i':
                return 'i'
            elif xp == 'i' or xn == 'i':
                return ' '
            else:
                return 'i'
        elif x == 'i':
            return 'T'
        else:
            return x

    def next(self):
        copy = list(self)
        for i in xrange(len(self)):
            self[i] = self._next(copy, i)
        return self


class Bars(SimpleBars):
    def _next(self, l, i):
        table = [{' ':' ', 'i':'T', 'T':'i', 'I':'I'},
                 {' ':'i', 'i':'I', 'T':' ', 'I':'T'}]
        def _is_black(c):
            return (c == 'i' or c == 'I')
        x = l[i]
        count = 0
        if _is_black(l[i-1]):
            count += 1
        if _is_black(l[(i+1) % len(l)]):
            count += 1
        return table[count % 2][x]



if __name__ == '__main__':
    bs = SimpleBars(' '*24)
    bs[8] = 'T'
    for i in range(30):
        print bs.next()

