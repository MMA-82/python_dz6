#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# import random
# list = []
# length = int(input('Задайте длину списка: '))
# sum = 0
# for i in range(length):
#     list.append(random.randint(0, 10))
#     if i % 2 == 1:
#         sum += list[i]
# print(list)
# print('Сумма элементов списка с нечетным индексом =', sum)

from random import randint as R
length = int(input('Задайте длину списка: '))
my_list = [R(0, 10) for _ in range(length)]
print(my_list)
nechet_list = [my_list[i] for i in range(len(my_list)) if i%2 == 1] 
print(f'Сумма элементов под нечетным индексом = {sum(nechet_list)}')