#Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.

# n = int(input('Введите число: '))
# list = []
# for i in range(1, n+1):
#     list.append(round((1 + 1/i)**i, 2))
# print(list)
# print('Суммма элементов списка:', round(sum(list), 2))

n = int(input('Введите число: '))
my_list = [round((1 + 1/i)**i, 2) for i in range(1, n+1)]
print(my_list)
print('Суммма элементов списка:', round(sum(my_list), 2))