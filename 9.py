# Тройка Пифагора — три натуральных числа a < b < c, для которых выполняется равенство
# a2 + b2 = c2
# Например, 32 + 42 = 9 + 16 = 25 = 52.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

for a in range(1, 1000):
    for b in range(1, 1000):
        c = int((a**2 + b**2)**0.5)
        if a < b < c and a**2 + b**2 == c**2 and a+ b + c == 1000:
            print(a, b, c)

            
# brute-force решение
def compute():
    PERIMETER = 1000
    for a in range(1, PERIMETER + 1):
        for b in range(a + 1, PERIMETER + 1):
            c = PERIMETER - a - b
            if a * a + b * b == c * c:
                return str(a * b * c)
if __name__ == "__main__":
    print(compute())            
