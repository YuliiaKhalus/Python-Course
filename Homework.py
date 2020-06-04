# Python Tasks #2
# task 1
b = int(input())
n = 0
while n <= b:
    m = 1
    while m <= b:
        print(m, end=' ')
        m += 1
    print('')
    b -= 1

# task 2
n = int(input())
while True:
    if n < 0:
        print(n)
        n += 1
    if n > 0:
        print(n)
        n -= 1
    if n == 0:
        break
print(0)

# task 3
n = int(input())
b = 0
result = 0
while b <= n:
    result = result + b
    b += 1
print(result)

# task 4
n = int(input())
b = 0
result = 0
while b <= n:
    if b % 2 != 0:
        result = result + b
    b += 1
print(result)

# the task from the class work
list_1 = []
list_2 = []
for i in range(5):
    n = int(input())
    if n > 0:
        list_1.append(n)
    if n < 0:
        list_2.append(n)
list_1.sort()
list_2.sort()
list_2.reverse()
list_3 = list_1 + list_2
print(list_3)

# Python Tasks #3
# task 1 Написати програму, яка парні числа замінить нулями, непарні підніме до квадрату.
list_1 = [2,3,4,5,6,]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        i = 0
        list_2.append(i)
    if i % 2 != 0:
        i = i ** 2
        list_2.append(i)
print(list_2)

# task 2 Написати програму, яка видаляє значення дублікати зі списку, тобто залишає значення в одному екземплярі.
list_3 = [2,2,5,7,8,8,9]
list_4 = []
for i in list_3:
    if i not in list_4:
        list_4.append(i)
print(list_4)

# task 3 Написати програму, яка знаходить у списку максимальне і мінімальне значення у списку.
list_5 = [3, 77, 43, 89, 5, 6,]
max_number = list_5[0]
min_number = list_5[0]
for i in list_5:
    if i > max_number:
        max_number = i
for i in list_5:
    if i < min_number:
        min_number = i
print(max_number, min_number)

# task 4 Написати програму, яка знаходить спільні значення з двох списків.
list_6 = [6,7,98,43,9,]
list_7 = [5,1,6,43,10,]
list_8 = []
for i in list_6:
    if i in list_7:
        list_8.append(i)
print(list_8)

