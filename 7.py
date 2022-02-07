A = [1]*1000000
A[0] = A[1] = summa = 0
for k in range (2,1000000,1):
    if A[k]:
        for m in range (2*k,1000000,k):
            A[m] = 0
        summa = summa + A[k]
    if summa == 10001:
        print (summa)
        print ("Наше число " + str(k))
        break

def is_simple(num):
    for i in range(1, 10+1):
        if num % i == 0 and i != 1 and i != num: return False
    return True
k = 0
num = 0
while k != 10001:
    if is_simple(num): k += 1
    num += 1
print(num-1)

from math import log

n = 1_000_000
summa = 1
if n > 1:
    cnt = int((log(n) + log(log(n)) - 0.5) * n) + 2 * n * (n < 26)
    print(cnt)

    A = [True] * cnt
    k = 1

    while summa < n:
        k += 2
        if A[k]:
            for m in range(k * k, cnt, 2 * k):
                A[m] = False
            summa += 1

else:
    k = 2

print(summa)
print("Наше число " + str(k))