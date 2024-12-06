# import time

# print(time.strftime('%H:%M:%S'))

# a = int(time.strftime('%H'))
# if(a<12):
#     print("good morning")
# elif(a<15):
#     print("good afternoon")
# else:
#     print("good night

# set ={}
# print(type(set))

# s1 = {1,2,3,4,5,6}
# s2 = {5,6,7,8,9,10}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2))
# print(s1.difference(s2))
# print(s1.isdisjoint(s2))
# print(s1.issubset(s2))
# print(s1.issuperset(s2))
# print(s1.add(7))
# print(s1.remove(7))
# print(s1.discard(6))
# print(s2.pop())
# s2.clear()
# print(s1)
# print(s2)

# l=[1,2,3,4,5,6,8]
# l1=list(map(lambda x:x*x, l))
# print(l1)
# print(list(filter(lambda x:x%2==0,l)))
# from functools import reduce
# print(reduce(lambda x,y: x+y,l))


# decorator 


def greed(fx):
    def mfx(*args, **kargs):
        print("welcome to the real world")
        fx(*args, **kargs)
        print("excaping the matrix")
    return mfx

# @greed
def addx():
    print("hello")
def add(a,b):
    print(a+b)

# addx()

greed(addx)()
greed(add)(1,2)

