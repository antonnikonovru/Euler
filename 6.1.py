a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = []
d = []
for i in range(a):
 i = i**2
c.append(i)
for j in range(b):
 d.append(j)

_sum_=(sum(c))
square=(sum(d)**2)
print(square - _sum_)

