#/usr/bin/python3
#!coding:utf-8
sum = 5                                                            # первоначальное значение суммы - 2 + 3 = 5
number = 2000000                                                   # сделаем скрипт универсальным и при этом простым: вместо 2 000 000 можно подставить любое число
for n in range(5, number, 2):                                      # начнём проверку на "простоту" с цифры 5, пропуская чётные цифры
    # print("Проверяю на \"простоту\' число {:d}.". format(n))     # опциональная строка для проверки корректности работы скрипта, информация излишняя
    k = 0
    i = 3
    while i * i <= n:
        # print("Проверяю делитель {:d}.".format(i))               # опциональная строка для проверки корректности работы скрипта, информация излишня
        if n % i == 0:
            # print("Число {:d} является делителем числа {:d}.\nСледовательно, число {} НЕ является простым.\n".format(i, n, n))
            k += 1
            break
        i += 2
    if k == 0:
        print("{:d} - число простое.".format(n))                   # опциональная строка для проверки корректности работы скрипта, информация излишня
        sum += n                                                   # сразу считаем сумму
# Ответ:
print("\nСумма всех простых чисел мен
