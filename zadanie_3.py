#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# x = input('Введите любое число: ')
# list = []
# for i in x:
#     if i.isdigit():
#         list.append(int(i))
# print('Сумма цифр числа равна:', sum(list))

number = input('Введите любое число: ')
list_numb = list(map(int, [i for i in number if i.isdigit()]))
print(f'Сумма цифр введенного числа = {sum(list_numb)}')