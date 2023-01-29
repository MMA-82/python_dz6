#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.

# import random
# my_list = []
# length = int(input('Задайте длину списка: '))
# part_list = []
# for i in range(length):
#     amount = random.randint(0, 2)
#     my_list.append(round(random.uniform(0, 10), amount))
#     if my_list[i] %1 != 0:
#         part = my_list[i] % int(my_list[i])
#         part_list.append(part)
# print(my_list)
# print('Разница между максимальным и минимальным значением дробной части элементов, отличной от 0 =', round(max(part_list) - min(part_list), 2))

import random 
length = int(input('Задайте длину списка: '))
my_list = [round(random.uniform(0, 10), 2) for _ in range(length)]
print(my_list)
my_list = list(filter(lambda x: x %1 != 0, my_list))
my_list = list(map(lambda x: x% int(x), my_list))
print('Разница между макс и мин дробной частью элементов, отличной от 0 =', round(max(my_list) - min(my_list), 2))
