

#2
print('Введіть значення і натисніть enter \nДля закінчення внесення данних натисніть enter')
a = int(input('-->>'))
numberList = []
while True:
    try:
        numberList.append(a)
        a = int (input('-->>'))
    except:
        break
print(numberList)

print('Середнє арефметияне списка ')

print(sum(numberList) / len(numberList))


#3
# s = 'Phython'
#
# print(s[:2] + s[5:])

# #4
# text = 'environment'
# print(text[0])
# b = text.replace(text[0], '_')
# print(b)

#5
# a = 'environment'
# print(a[2])
# b = a.replace(a[2], '')
# print(b)

#6
# a = (input('-->>'))
# d = (a[1:len(a)-1])
# print('result:')
# print(a[len(a)-1],d,a[0])

# lst = [1,2,3,4,5,6,7,8]
# sum(lst[::3])