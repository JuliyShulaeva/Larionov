# Вариант 19
from mpmath import matrix
import time


def read(f):
    #n_n, n_p = map(int, f.readline().split(' '))
    # print('n_num = ', n_num)
    # print('n_proc = ', n_proc)
    out = []
    for line in f:
        row = [int(i) for i in line.split()]
        out.append(row)
    return out


def cons(o1, p11):
    b = matrix(o1)
    # print('b = ',o)
    c = matrix(p11)
    # print('c = ', c)
    a = b * c
    # print('a = ', a)
    return a


start_time = time.time()
f = open('text1.txt')
b = []
o = read(f)
n = len(o)
#p1_1 = o.pop()
p1 = o.pop(n - 1)
#print('p1 = ', p1)
p0 = o.pop(0)
#print('p0 = ', p0)
#print('o = ', o)

a = cons(o, p1)
print('a = ', a)

time = time.time()
print('time = ', time)

f.close()