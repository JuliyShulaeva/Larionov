import time


def pref(array):
    array1 = []
    q=0
    for u in array:
        q=q+u
        array1.append(q)
    return array1


if __name__ == "__main__":
    start_time = time.time()
    f = open('text.txt', 'r')
    u = 1
    mass = []
    mass1 = []
    mass2 = []
    mass3 = []
    mass4 = []
    n_num, n_proc = map(int, f.readline().split(' '))
    #print('n_num = ', n_num)
    #print('n_proc = ', n_proc)
    array01 = map(int, f.readline().split(' '))
    #print('array01 = ', array01)
    for t, i in enumerate(array01):
            mass.append(i)
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

    mass1 = pref(mass)
    print('mass1 = ',mass1)
    o = len(mass1)
    #print('o = ',o)
    #print("mass1 = ", mass1)
    mass2 = mass1[::-1]
    mass3 = mass2[::2]
    #print("mass2 = ", mass2)
    #print("mass3 = ", mass3)

    for y in mass2:
        e = y + p1
        mass4.append(e)
    print('mass4 = ', mass4)
    time = time.time()
    print('time = ', time)
    f.close()