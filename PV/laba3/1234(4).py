import time
from multiprocessing import Pool
from mpmath import matrix
import numpy as np


def compos(ar):
    #start_time = time.time()
    shared_array, vector , interv = ar
    mass = []
    index1 = list(interv)
    a = shared_array[index1[0]:index1[1]+1]

    b = matrix(a)
    # print('b = ',o)
    c = matrix(vector)
    # print('c = ', c)
    g = b * c
    # print('g = ', g)

    t = np.array(g, dtype=int)
    time12 = time.time()
    #print('time = ', time12)

    return t, time12


def make_intervals(n_n, n_p):
    step = n_n // n_p
    #print('Чисел в потоке = ', step)

    i = 0
    n_intr = 0
    inter = []

    while n_intr < n_p:
        if n_intr == n_p - 1:
            inter.append([i, n_n - 1])
        else:
            inter.append([i, i + step - 1])
        n_intr += 1
        i += step

    return inter


def read(f):
    out = []
    for line in f:
        row = [int(i) for i in line.split()]
        out.append(row)
    return out


if __name__ == "__main__":

    f = open('text1.txt', 'r')

    intervals = []
    numbers1 = []
    mass = []

    b = []
    o = read(f)
    #print('o = ', o)
    p0 = o.pop(0)
    #print('p0 = ', p0)
    p0_0 = list(p0)
    n_num = p0_0[0]
    #print('n_num = ', n_num)
    n_proc = p0_0[1]
    #print('n_proc = ', n_proc)
    n = len(o)
    #print('n = ', n)
    p1 = o.pop(n - 1)
    #print('p1 = ', p1)

    intervals = make_intervals(n_num, n_proc)
    #print('intervals = ', intervals)

    pool = Pool(n_proc)
    map_data = [(o, p1, interval) for interval in intervals]
    otv = pool.map(compos, map_data)
    #print('otv = ', otv)

    o = list(otv)
    #print('o = ', o)

    obj_1 = o[0]
    #print('obj_1 = ', obj_1)
    obj_1_1 = list(obj_1)
    #print('obj_1_1 = ', obj_1_1)
    t_1 = obj_1_1[0]
    print('t_1 = ', t_1)
    time1 = obj_1_1[1]
    print('time1 = ', time1)
    a = 0
    t1 = list(t_1)
    #print('t1 = ', t1)
    for u1 in t1:
        a = a + u1
    print('a = ', a)
    print()

    obj_2 = o[1]
    #print('obj_2 = ', obj_2)
    obj_2_1 = list(obj_2)
    #print('obj_2_1 = ', obj_2_1)
    t_2 = obj_2_1[0]
    print('t_2 = ', t_2)
    time2 = obj_2_1[1]
    print('time2 = ', time2)
    b = 0
    t2 = list(t_2)
    #print('t1 = ', t1)
    for u2 in t2:
        b = b + u2
    print('b = ', b)
    print()

    obj_3 = o[2]
    #print('obj_3 = ', obj_3)
    obj_3_1 = list(obj_3)
    #print('obj_3_1 = ', obj_3_1)
    t_3 = obj_3_1[0]
    print('t_3 = ', t_3)
    time3 = obj_3_1[1]
    print('time3 = ', time3)
    c = 0
    t3 = list(t_3)
    # print('t1 = ', t1)
    for u3 in t3:
        c = c + u3
    print('c = ', c)
    print()

    obj_4 = o[3]
    #print('obj_4 = ', obj_4)
    obj_4_1 = list(obj_4)
    #print('obj_4_1 = ', obj_4_1)
    t_4 = obj_4_1[0]
    print('t_4 = ', t_4)
    time4 = obj_4_1[1]
    print('time4 = ', time4)
    d = 0
    t4 = list(t_4)
    # print('t1 = ', t1)
    for u4 in t4:
        d = d + u4
    print('d = ', d)
    print()

    # total_amount = a + b + c + d
    # print('total_amount = ', total_amount)

    times = time1 + time2 + time3 + time4
    print('times = ', times)

    acceleration = times / 1526103138.173861
    print('acceleration = ', acceleration)

    f.close()