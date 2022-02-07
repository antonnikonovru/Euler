num1 = 999
num2 = 999
polist = list()
i = 0

while num2 > 316:
    pol = num1 * num2
    pol1 = pol // 1000
    pol2 = pol % 1000
    revpol2 = int(str(pol2)[::-1])
    if pol1 == revpol2 and pol > 100000:
        polist.insert(i, pol)
        i += 1
    num1 -= 1
    if num1 < 316:
        num1 = 999
        num2 -= 1

polist.sort(reverse=True)
print(polist[0])

a1 = 999
aMin = 100
polindrom = 0
while a1 > aMin:
a2 = a1
while a2 > aMin:
pol = a1 * a2
if str(pol) == str(pol)[::-1] and pol > polindrom:
polindrom = pol
aMin = a2
break
a2 -= 1
a1 -= 1
print(polindrom)