#1
# a = []
#
# if not a: print('список порожній')
# elif a: print('в списку є значення')

#2
# a = []
#
# lst = ["1", "2", "3", "33333", "white", "yellow", "red", "all123"]
# lst_str = []
# def separate_list(lst):
#     for item in lst:
#         if item.isalpha():
#             lst_str.append(item)
# print(item)
#
# import string




#3
# a_list = ["Red","Green","White","Black", "Pink","Yellow"]
# print( [x for x in a_list if len(x)<5] )

#4
# print('Введіть число і натисніть enter для довадання \nЩоб знайти суму натисніть enter')
# a = int(input('-->>'))
# b = []
# while True:
#     try:
#         b.append(a)
#         a = int (input('-->>'))
#     except:
#         break
# def list_sum(lst):
#     s = 0
#     for i in lst:
#         s = s + i
#     return s
#
# print(list_sum(b))

#5
# print('Введіть число і натисніть enter для меження \nЩоб знайти добуток натисніть enter')
# a = int(input('-->>'))
# b = []
# while True:
#     try:
#         b.append(a)
#         a = int (input('-->>'))
#     except:
#         break
# def multiply(lst):
#     s = 1
#     for i in lst:
#         s *= i
#     return s
#
# print(multiply(b))

#6
# print("Щоб дізнатися чи білет є щасливис введіть його номер")
# a = [int(i) for i in input('-->>')]
# if sum(a[:3]) == sum(a[3:]):
#     print('щасливий')
# else:
#     print('не щасливий')
#6.1
# def luckyTickets(num):
#   if num % 2 != 0 or num <= 0: return '# Error: invalid number'
#   array = [1] * 10 + [0] * (num // 2 * 9 - 9)
#   for i in range(num // 2 - 1):
#     array = [sum(array[x::-1]) if x < 10 else sum(array[x:x-10:-1]) for x in range(len(array))]
#   return sum([x**2 for x in array])
#
# # количество счастливых билетов среди шестизначных чисел
# print(luckyTickets(6))

#8
# lst_1 = [1, 2, 3]
# lst_2 = [4, 5, 6]
# lst_3 = lst_1 + lst_2
# print(lst_3)

#9

# def a():
#     for i in range(1, 11):
#         print(' ' * (10 - i), '* ' * i)
#
# print(a())








