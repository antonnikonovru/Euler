d = 0
for f in range(1, 101):
    d += f ** 2
g = 0
for t in range(1, 101):
    g += t
i = g ** 2 - d
print(i, d)
