import numpy as np  # импортируем нампай и назначаем псевдоним


f = open('text2.txt', 'w')
a = np.random.randint(0, 10, (11, 10))
print('a==', a)

for item in a:
    f.write("%s\n" % item)

f.close()
