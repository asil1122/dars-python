import os
from math import *
import random
os.system(("cls"))
        #=====R1=====#
"""
lst=[1,2,3,4,5]
print(list(map(lambda x:float(x),lst)))
"""
        #=====R2=====#
"""
def b(son:float,son1:float,x:str):
    if x == '*':
        return son*son1
    elif x == "/":
        return son/son1
a = input("kiriting:")
print(a)
lst = list(map(lambda x: float(x) if x.isdigit() else x, a))
print(lst)
for i in range(lst.count(" ")):
   lst.remove(" ")
if len(lst) < 3 :
    raise ValueError("3 dan kamroq")
elif lst[1] == '+':
    raise ValueError("2-index '+' ")
elif lst[1] == '-':
    raise ValueError("2-index '-'")
print(b(lst[0], lst[2], lst[1]))
"""
        #=====R3=====#
"""
lst=[("Eshmatov Toshmat", "21.10.2007",7000000),("Kimdurov Kim","01.01.2007",16000000)]
lst1=list(map(lambda x: x[0],lst))
lst2=list(map(lambda x: x[1],lst))
lst3=list(map(lambda x: x[2],lst))
print(lst1)
print(lst2)
print(lst3)
"""
        #=====R4=====#
"""
def oq(son:list,lst:list):
    for i in son:
        if i in lst:
            son.remove(i)
    return son
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [2, 4, 6, 8]
print(list(filter(lambda x: x not in lst2, lst)))
"""
        #=====R5=====#
"""
social = ["Instgram", "Facebook", "Telegram", "Tik-Tok", "Radiogram"]

search = 'ok'
print(list(filter(lambda x: search in x, social)))
"""
        #=====2-MISOL=====#
"""
lst = [1.7, 2.6, -3.2, 4.3, -6.1, 7.8, -1.5]
print(list(map(lambda x: ceil(x) ,lst)))
"""
        #=====3-MISOL=====#
"""
lst = [1.7, 2.6, -3.2, 4.3, -6.1, 7.8, -1.5]
print(list(map(lambda x: floor(x) if x > 0 else x,lst)))
"""
        #=====4-MISOL=====#
"""
lst=list(map(lambda x:0-int(x) if int(x) > 0 else int(x)*2,input("son kiriting:").split()))
print(lst)
"""
        #=====5-MISOL=====#
"""
n = int(input("soni kiriting:"))
lst=list(filter(lambda x: pow(n,3)<int(x) ,input().split()))
print(lst)
"""
        #=====6-MISOL=====#
"""
lst = list(filter(lambda x: not float(x)-floor(float(x)), input("sonlar kiriting:").split()))
print(lst)
"""
        #=====9-MISOL=====#
"""
print(list(filter(lambda x: int(x)>0, input("sonlar kiriting:").split())))
"""