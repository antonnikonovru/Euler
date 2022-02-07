sum1 = 0
sum2 = 0

for x in range(1, 1000001):
    sum1 += x ** 2
    sum2 += x
sum2 **= 2

total = sum2 - sum1
print(total)

sqr1 = list(range(1, 101))
sqr2 = [n ** 2 for n in sqr1]
sumsqr = sum(sqr2)

sqr3 = list(range(1, 101))
sqrsum = sum(sqr3)
sqrsum *= sqrsum

diff = sqrsum - sumsqr
print(diff)

lister = [i**2 for i in range(101)]
lister2 = [i for i in range(101)]
print((sum(lister2))**2 - sum(lister))

