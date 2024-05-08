# Question 1.1
def memory(n):
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

f = memory(10)
f(lambda x: x*2)
f(lambda x: x-7)
f(lambda x: x > 5)
f(lambda x: type(x))


# Question 2.1
s1 = [1, 2, 3]
s2 = s1
s1 is s2
s2.extend([5, 6])
s1.append([-1, 0, 1])
s3 = s2[:]
s3.insert(3, s2.pop(3))
s1[:3] == s2[:3]


# Question 2.3
def group_by(s, fn):
    """_summary_

    Args:
        s (_type_): _description_
        fn (function): _description_
    >>> group_by([12, 23, 14, 45], lambda p: p//10)
    {1: [12, 14], 2: [23], 4: [45]}
    """
    grouped = {}
    for v in s:
        key = fn(v)
        if key in grouped:
            grouped[key].append(v)
        else:
            grouped[key] = [v]
    return grouped

group_by([12, 23, 14, 45], lambda p: p//10)
group_by(range(-3, 4), lambda x: x * x)


# Question 2.4
def add_this_many(x, el, s):
    """Add EL to the end of S as the number of times X occurs in S
    """
    times = sum([i == x for i in s])
    s.extend([el]*times)

s = [1, 2, 4, 2, 1]
add_this_many(1, 5, s)
s
add_this_many(2, 2, s)
s



# Quesiton 4.1
def filter(iterable, fn):
    """Only yields elements when fn(elem) == True
        
    """
    for x in iterable:
        if fn(x):
            yield x
            
is_even = lambda x: x % 2 == 0
list(filter(range(5), is_even))

all_odd = (2*y-1 for y in range(5))
list(filter(all_odd, is_even))

naturals = (n for n in range(1, 100))
t = filter(naturals, is_even)
next(t), next(t)


# Question 4.2
def merge(a, b):
    i, j = next(a), next(b)
    
    try:
        while 1:
            if i < j:
                yield i
                i = next(a)
            elif i > j:
                yield j
                j = next(b)
            else:
                yield i
                i, j = next(a), next(b)
    except StopIteration:
        print("this is the end")
    
def sequence(start, step):
    while 1:
        yield start
        start += step
        

a = sequence(2, 3)
b = sequence(3, 2)
#[next(a) for _ in range(5)], [next(b) for _ in range(5)]

result = merge(a, b)
[next(result) for _ in range(10)]

list(merge(iter([1, 5, 10]), iter([1, 2, 3, 5, 10])))