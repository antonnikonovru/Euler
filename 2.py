f = [1, 2]
a = 0
s = 0 # summ
for i in f:
    c = (f[a] + f[a + 1])
    if c < 4000000:
        f.append(c)
        a += 1
for i in f:
    if i % 2 == 0:
        s = s + i
print(s)

a = 1
b = 2
s = b
while b < 4*10**6:
    a = a + b
    b = a + b
    s += b

print(s)

s, a, b = 0, 1, 2
while b < 4*10**6:
    if b % 2 == 0:
        s += b
    a, b = b, a + b

print(s)

fib = [1, 2]
sum = 2

while True:
    fib.append(fib[-1] + fib[-2])

    if fib[-1] > 4000000:
        break

    if fib[-1] % 2 == 0:
        sum += fib[-1]

print(sum)

s = [1, 2]

for i in s:
    i += s[-1]
    s.extend([i])
    a = 0
    for i in s:
        if i % 2 == 0:
            a += i
    if i >= 4000000:
        break

print(a)

f = [1, 2]
a = 0
s = 0 # summ
for i in f:
    c = (f[a] + f[a + 1])
    if c < 4000000:
        f.append(c)
        a += 1
for i in f:
    if i % 2 == 0:
        s = s + i
print(s)
