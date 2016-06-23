import time
import sys

t0   = time.time()
s    = t0
page = 0

with open('log'+str(t0)+'.txt','w') as fobj:
    while(True):
        c = sys.stdin.readline()
        if len(c) == 0 or c[0] == 'q':
            break
        elif c[:-1].isnumeric():
            page = int(c)
        else:
            page += 1
        t1 = time.time()
        fobj.write('{0} {1}\n'.format(page,t1-t0))
        print(page,t1-t0)
        t0 = t1
    page += 1
    t1 = time.time()
    fobj.write('{0} {1}\n'.format(page,t1-t0))
    print(page,t1-t0)
    fobj.write('total {0}\n'.format(t1-s))
    print('total',t1-s)
