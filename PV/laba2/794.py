import time
from multiprocessing import Pool


def pref(ar):
    mass1 = []
    q = 0

    shared_array, interv = ar

    index1 = list(interv)
    a = shared_array[index1[0]:index1[1]+1]

    for u in a:
        q = q + u
        mass1.append(q)
    #print('mass1 = ', mass1)

    time12 = time.time()
    #print('time = ', time12)

    return mass1, time12


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


if __name__ == "__main__":
    start_time = time.time()
    f = open('text.txt', 'r')

    intervals = []
    numbers1 = []
    mass = []

    n_num, n_proc = map(int, f.readline().split(' '))
    # print('n_num = ', n_num)
    # print('n_proc = ', n_proc)
    array01 = map(int, f.readline().split(' '))
    # print('array01 = ', array01)
    intervals = make_intervals(n_num, n_proc)
    # print('intervals = ', intervals)

    for t, i in enumerate(array01):
        mass.append(int(i))
        if t == n_num - 1:
            break
        #print('mass = ', mass)

    p2 = len(mass)
    #print('len = ',p2)
    p1 = mass.pop(p2 - 1)
    #print('p1 = ',p1)
    #print('mass = ', mass)
    mass.insert(p2 - 1, p1)
    #print("mass = ", mass)

    pool = Pool(n_proc)
    map_data = [(mass, interval) for interval in intervals]
    otv = pool.map(pref, map_data)
    #print('otv = ', otv)

    o = list(otv)
    #print('o = ', o)

    obj = o[0]
    #print('obj = ', obj)
    obj_01 = list(obj)
    array02 = obj_01[0]
    #print('array02 = ', array02)
    times_1 = obj_01[1]
    #print('times_1 = ', times_1)

    pi = len(array02)
    #print('pi = ', pi)
    pi_1 = array02.pop(pi - 1)
    #print('pi_1 = ', pi_1)
    array02.insert(pi - 1, pi_1)
    #print('array02 = ',array02)

    obj_1 = o[1]
    #print('obj_1 = ', obj_1)
    obj_1_01 = list(obj_1)
    array_1_02 = obj_1_01[0]
    #print('array_1_02 = ', array_1_02)
    times_1_1 = obj_1_01[1]
    #print('times_1_1 = ', times_1_1)

    times_2 = times_1 + times_1_1
    #print('times_2 = ', times_2)

    ijouib = []
    array_1_02_b = []

    for h in array_1_02:
        i = 0
        i = h + pi_1
        array_1_02_b.append(i)
    #print('array_1_02_b = ', array_1_02_b)

    mass1 = []
    mass1 = array02 + array_1_02_b
    #print('mass1 = ', mass1)

    mass2 = []

    mass2 = mass1[::-1]
    mass3 = mass2[::2]
    #print("mass2 = ", mass2)
    #print("mass3 = ", mass3)

    mass4 = []

    for y in mass2:
        e = y + p1
        mass4.append(e)
    #print('mass4 = ', mass4)

    accel = times_2 / 1524893871.973438
    print('accel = ', accel)

    f.close()