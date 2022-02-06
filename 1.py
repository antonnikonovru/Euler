print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
print(sum(set(list(range(0, 1000, 3)) + list(range(0, 1000, 5)))))
print(sum([a for a in range(1000) if a % 3 == 0 or a % 5 == 0]))
