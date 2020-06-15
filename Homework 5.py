def func_1(a,n=3):
    unique_items = set(a)
    max_values = []
    for i in range(n):
        max_values.append(max(unique_items))
        unique_items.remove(max(unique_items))
    return max_values

l = [2,5,9,0,0,33,66,1,77,9]
print(func_1(l))


def func_2(a,b):
    set_a = set(a)
    set_b = set(b)
    output = list(set_a.intersection(set_b))
    return output

l1 = [1,2,3,4,5,7,1,2,4,6]
l2 = [1,7,9,0,0,0,2,4,4,4]
print(func_2(l1,l2))


def func_3(a):
    numbers = []
    n = 0
    while n < a:
        numbers.append(n)
        n += 1
    return numbers

print(func_3(4))


def func_4(dict1):
    keys = tuple(list(dict1.keys())[::-1])
    values = list(dict1.values())[::-1]
    new_dict = dict(zip(keys, values))
    return new_dict

d = {1:1,
      0:0,
      2:2,
      3:3
}
print(func_4(d))


def func_5(n):
    keys = tuple(set(n.lower()))
    values = []
    for i in keys:
        value = n.lower().count(i)
        values.append(value)
    d = dict(zip(keys, values))
    return d

print(func_5('laLAlaTrataTANana'))


def func_6(*a):
    for i in a:
        print(i)

func_6(6,7,7,1,2,3,5,6,8,)

sum = 0
def func_7(n):
    global sum
    sum += n
    if n == 0:
        return sum
    func_7(n-1)
    return sum

print(func_7(int(input())))


def func_8(x):
    y1 = x**2 - x - 1
    y2 = x**3 - 4*(x**2) - 4*x + 1
    return y1, y2

print(func_8(2))


def func_9(a,b):
    if a == 0:
        return None
    else:
        x = b/a
        return x

print(func_9(6,8))


def func_10(a,b,c,d=0):
    disc = b**2 - 4*a*c
    if disc < 0:
        return None
    elif disc == 0:
        x = -(b/(2*a))
        return x
    elif disc > 0:
        x1 = (-b - (disc**0.5))/(2*a)
        x2 = (-b + (disc**0.5))/(2*a)
        return x1, x2

print(func_10(3,-2,-16))


def func_11(a,b,c,d=0):
        def inner():
            x = int(input())
            nonlocal a
            nonlocal b
            nonlocal c
            y = a*(x**2) + b*x + c
            return y
        return inner()

print(func_11(-2,3,-2))



