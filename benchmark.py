#!/usr/bin/env python

import noeq

def test(n):
    c = noeq.Noeq("",'localhost:4444')
    c.connect()
    c.get(n)

if __name__ == '__main__':
    import timeit
    loops = 1000
    for n in (1,2,3,5,8,13,21,34,55):
        out = timeit.timeit('test({})'.format(n), setup="from __main__ import test", number=loops)
        perloop = out / loops
        perone = perloop / n
        print "Gen {}: {:.2f} ms/op {:.2f} ms/id".format(n, perloop * 1000000, perone * 1000000)
