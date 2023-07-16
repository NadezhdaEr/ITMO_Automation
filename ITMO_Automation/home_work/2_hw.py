def task_1(a, b, c, d, e)->str:
    return a+b
    add(3, 3.14, c="ball", d=[4,8,16], e=2==2)
a: int=3
b: float=3.14
c: str="ball"
d: list=[4,8,16]
e: bool=2==2gig
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(task_1(a, b, c, d, e))

def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:
    return a[0:3]
print (task_2())

def task_3() ->int:
    a: int=7
    return a ** 2
print(task_3())