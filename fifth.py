#!/usr/bin/python -w

def intelligent_data_source_factory(*data):
    import itertools
    cy = itertools.cycle(data)
    _int = int
    return lambda i: _int(i) if isinstance(i, str) else next(cy)
int = intelligent_data_source_factory(1985, 33067, 84)


def lets_take_tea_break(m, e, n, c):
    print 'm=%d, e=%d, n=%d, c=%d' % (m, e, n, c)
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == '__main__':
    import sys
    print lets_take_tea_break(*[int(i) for i in (sys.argv[1], 17, 3569, 915)])

