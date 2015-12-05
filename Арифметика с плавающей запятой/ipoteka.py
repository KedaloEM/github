__author__ = 'Егор'

from decimal import Decimal

print('сумма  ', ' проценты в форме 0,**   ', 'срок(лет)  ', '(по отдельностив каждой строчке)')
S0, x, y = int(input()), float(input()), int(input())
alpha = float((12 + x) / 12)
n = 12 * y
platezh = Decimal(S0 * (x / 12 + (x / 12) / ((1 + x / 12) ** (y * 12) - 1))).quantize(
    Decimal('0.01'))  #ежемесячная выплата
summaost = S0 * (x / 12 + (x / 12) / ((1 + x / 12) ** (y * 12) - 1))
print('размер аннуитетного платежа исходя из необходимости погасить кредит за', y, 'лет', platezh)
print('суммарную переплату относительно начальной суммы кредита', platezh * n - S0)

#таблица
mass = [[0] * 4 for i in range(n + 1)]
ostatok = []
ostatok.append(S0)
mass[0][0] = 'Выплата'
mass[0][1] = 'Остаток'
mass[0][2] = 'На %'
mass[0][3] = 'На сумму долга'
for i in range(1, n + 1):
    ostatok.append(ostatok[i - 1] * alpha - summaost)
    if platezh < ostatok[i - 2] * alpha - summaost:
        mass[i][0] = platezh
        mass[i][1] = Decimal(ostatok[i - 1] * alpha - summaost).quantize(Decimal('0.01'))
        mass[i][2] = Decimal(ostatok[i - 1] * (x) / 12).quantize(Decimal('0.01'))
        mass[i][3] = Decimal(summaost - ostatok[i - 1] * (x) / 12).quantize(Decimal('0.01'))
    else:
        mass[i][0] = Decimal(ostatok[i - 2] * alpha - summaost).quantize(Decimal('0.01'))
        mass[i][1] = 0
        mass[i][2] = Decimal(ostatok[i - 1] * (x) / 12).quantize(Decimal('0.01'))
        mass[i][3] = Decimal(ostatok[i - 1] - ostatok[i - 1] * (x) / 12).quantize(Decimal('0.01'))

ostatok.pop()

for row in mass:
    for elem in row:
        print(elem, end='    ')
    print()

import numpy as np
import matplotlib.pyplot as plt

#график остатка (в целом)
month = []
for i in range(1, n + 1):
    month.append(i)

plt.subplot(2, 2, 1)
plt.plot(month, ostatok)
plt.xticks(month, month)
plt.ylabel('Ostatok')
plt.xlabel('Month')
plt.title('Ostatok po creditu')
plt.subplots_adjust(left=0.15)

plt.subplot(2, 2, 2)
proz = []
for i in range(1, n + 1):
    proz.append(mass[i][2])
plt.plot(month, proz)
plt.xticks(month, month)
plt.ylabel('Na procenty')
plt.xlabel('Month')
plt.title('Pogashenie procentov')
plt.subplots_adjust(left=0.15)

plt.subplot(2, 2, 3)
basic = []
for i in range(1, n + 1):
    basic.append(mass[i][3])
plt.plot(month, basic)
plt.xticks(month, month)
plt.ylabel('Na osnovnuyu summu')
plt.xlabel('Month')
plt.title('Pogashenie osnovnoy summy')
plt.subplots_adjust(left=0.15)
plt.show()
