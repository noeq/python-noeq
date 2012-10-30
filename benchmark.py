#!/usr/bin/env python

import noeq

client = noeq.Noeq("",'localhost:4444')
client.connect()

def test(n):
    client.get(n)

if __name__ == '__main__':
    import timeit
    loops = 50000
    print "Testing with {} loops:".format(loops)
    for n in (1,2,3,5,8,13,21,34,55):
        out = timeit.timeit('test({})'.format(n), setup="from __main__ import test", number=loops)
        perloop = out / loops
        perone = perloop / n
        print "Generate {:>2} ids: {:>10.2f} ms/op {:>10.2f} ms/id {:>10} ids/s".format(n, perloop * 1000000, perone * 1000000, int(round(1 / perone)))
