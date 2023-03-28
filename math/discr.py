import math

#ax2 + bx + c = 0

a = float(input('Коэф. а = '))
b = float(input('Коэф. b = '))
c = float(input('Коэф. c = '))

#D = b2 - 4ac
discr = (b ** 2 - 4 * a * c)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print('Корень x1 = ', x1,
          '. Корень х2 = ', x2)
elif discr == 0:
    x = -b / (2 * a)
    print('Корень x = ', x)
elif discr < 0:
    print('Корня нет')

print(discr)