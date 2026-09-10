'''def sum(*a):
    total=0
    for i in a:
        total=total+i
    print(total)
sum(10,20,30,40)'''

'''
def q(*a):
    print(set(a))
q(10,20)'''
''''''''

'''l1=[10,20,30]
def add(l2):
    return sum(l2)
print(add(l1))
'''

'''def sum(a,b):
    c=a+b
    return c
def mul(a,b):
    return a*b
def mainlogic():
    x=sum(10,20)
    u=mul(94,3)
    print(x)
    print(u)
mainlogic()'''

'''def hello(name):
    message=f"Hello {name}"
    def display():
        print(message)
    return display

h=hello("deedpla")
h()'''

'''def mydesign(func):
    def wraper():
        print("hello")
        func()
        print("after")
    return wraper
def hello():
    print("hello guys")
m=mydesign(hello)
m()'''

'''import math
print(math.sqrt(5))
print(math.pow(2,3))
print(math.log(2,3))
print(math.factorial(5))
print(math.__doc__)
print(dir(math))
print(len(dir(math)))'''

'''import random
print(random.uniform(10,20))'''

import random
print(random.randrange(1,10,2))


