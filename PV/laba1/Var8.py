import time


strog = []
kol = 0
kol1 = 0
f = open('text.txt', 'r')
a = f.readline().split(' ')
numbers_in_the_array = int(a[0])
number_of_processors = int (a[1])
print('Чисел в массиве = ', numbers_in_the_array)
# print('Количество процессоров = ', number_of_processors)
ch = int(input('Задайте число для сравнения - '))
# print('Число для сравнения - ', ch)
for el in f:
    strog = el.split(' ')
array = []
for i, t in enumerate(strog):
    # print(i, t)
    array.append(t)
    if i == numbers_in_the_array-1:
        break
for m in array:
    m = int(m)
    if m >= ch:
         kol += 1
one_thread_running_time = time.time()
print(' thread_running_time = ', one_thread_running_time)
# print('strog = ', array)
print('kol = ', kol)
f.close()
