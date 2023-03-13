def add(*args):
    sum = 0
    print(type(args))
    for i in args:
        sum += i
    return sum

ans = add(1,6,8,6,3,4,7,9,6,1,4,5,3,8)
print(ans)


def func(n,**kwargs):
#     print(kwargs)
#     for (key,value) in kwargs.items():
#         print(key)
#         print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    return(n)



print(func(2,add=3,multiply=9))
