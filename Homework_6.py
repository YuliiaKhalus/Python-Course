import functools
# Task 1.


def dec1(func):
    @functools.wraps(func)
    def inner(a, b):
        if b == 0:
            print('Invalid Value')
            return float('nan')
        return func(a,b)
    return inner


@dec1
def func_9(a, b):
    if a == 0:
        return None
    else:
        x = b/a
        print(x)
        return x


func_9(0, 7)

# Task 2


def dec2(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(args, str(kwargs))
        print(func(*args, **kwargs))

    return inner


@dec2
def func_9(a, b):
    if a == 0:
        return None
    else:
        x = b/a
        return x


func_9(6, b=5)

# Task 3. cache for fibonacci func


def cache(func):
    d = {}
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in d:
            return d.setdefault(key)
        else:
            d.update({key: func(*args, **kwargs)})
            return func(*args, **kwargs)

    return inner


@cache
def fib1(n):
    a, b = 0, 1
    while n:
        a, b = b, a+b
        n -= 1

    return a


print(fib1(50))
print(fib1(50))
print(fib1(122))
print(fib1(122))
print(fib1(122))
print(fib1(50))
print(fib1(134))
print(fib1(134))

# Task 4. HTML tags


def format_with_u_tag(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        text = func(*args, **kwargs)
        return f'<u>{text}</u>'

    return inner


def format_with_b_tag(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        text = func(*args, **kwargs)
        return f'<b>{text}</b>'

    return inner


def format_with_i_tag(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        text = func(*args, **kwargs)
        return f'<i>{text}</i>'

    return inner


def text(a):
    return str(a)


print(format_with_b_tag(text)(4))
print(format_with_i_tag(text)(4))
print(format_with_u_tag(text)(4))


# Task 5
def dec_factory(a):
    if callable(a):
        @functools.wraps(a)
        def inner(b):
            print(b)
        return inner
    if not callable(a):
        def decorator(func):
            @functools.wraps(func)
            def inner(b):
                print(a*b)
            return inner
        return decorator


@dec_factory
def func1(number):
    return number


@dec_factory(5)
def func2(number):
    return number


func1(6)
func2(6)







