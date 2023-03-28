import math

A = int(input('Длина 1 катета: '))
B = int(input('Длина 2 катета: '))

C = int(math.sqrt(A ** 2) +(B ** 2))

print('Тип переменной: ', type(A))
print('Гипотенуза равна: ', C)