from multiprocessing import Pool
import time


def task(arys):
    shared_array, interv, n = arys
    kol_local = 0

    index1 = list(interv)
    a = shared_array[index1[0]:index1[1]+1]
    # print('a = ', a)

    for m in a:
        if m >= n:
            kol_local += 1
    # print(kol_local)

    thread_running_time = time.time()
    print(' thread_running_time = ',  thread_running_time)

    return kol_local, thread_running_time


def make_intervals(n_n, n_p):
    step = n_n // n_p
    print('Чисел в потоке = ', step)

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
    intervals = []
    numbers1 = []
    f = open('text.txt', 'r')  # 1495260

    ch = int(input('Задайте число для сравнения - '))

    n_num, n_proc = map(int, f.readline().split(' '))
    #numbers = f.readline().split(' ')
    #len_1 = len(numbers)
    #print('len = ', len_1)
    numbers = map(int, f.readline().split(' '))

    intervals = make_intervals(n_num, n_proc)
    # print('intervals = ', intervals)

    for t, i in enumerate(numbers):
        # print('1 = ', t, i)
        numbers1.append(i)
        # print('numbers1 = ', numbers1)
        if t == n_num - 1:
            break

    pool = Pool(n_proc)
    map_data = [(numbers1, interval, ch) for interval in intervals]
    otv = pool.map(task, map_data)
    print('otv = ', otv)

    index2 = list(otv)
    print('index2 = ', index2)
    by = []
    for line in index2:
        for c in line:
            by.append(c)

    print('by = ', by)
    ch = []
    ch = by[0],by[2],by[4],by[6]
    print (ch)
    u = 0
    for ij in ch:
        u += ij
    print(u)

    ch1 = []
    ch1 = by[1], by[3], by[5], by[7]
    print(ch1)
    u1 = 0
    for ij1 in ch1:
        u1 += ij1
    print(u1)

    u2 = u1 / 1522479736.4542093
    print(u2)
    #number = 0
    #for i in index2[1]:
        #number += i

    #print('number = ', number)
    f.close()