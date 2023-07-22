        #=====1-misol======#
"""
lst = [(11,22,33,44),(55,66,77,88),(99,101,110,120),(130,140,151,161)]
print(*lst[0])
print(*lst[1])
print(*lst[2])
print(*lst[3])
print("summasi=",sum(lst[0]+lst[1]+lst[2]+lst[3]))
"""

        #=====Q-12-misol=====#
"""
list = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
count = 0   
for i in list:                                           
    if type(i) == int:
       count+=1
print(count,"ta integer bor")
"""
        #=====Q-13-misol=====#                                                       
"""                                                   
lst = [5, 'ab', 3, 89, 4, 'xyy', 5, 'ppp', 8, -5, -120]
max = 0
for i in lst:
    if isinstance(i, int) or isinstance(i, float):         
        if i > max:
             max=i
print(max)
"""
        #=====Q-14-misol=====#
"""
lst,natija = [1,6,6,6], 7
for i in lst:
    natija = natija * (10 ** len(str(i))) + i              
    natija=natija+1
natija=(" ".join(str(natija))).split()
print(f"{natija}")
"""
        #=====Q-15-misol=====#
"""
lst=list(map(int,input("Sonlar kiriting: ").split()))
a = 0
b = 0
for i in lst:
     if i > a:                                               
       a = i
       b+=1
if b == len(lst):
    print("Tartibli")
else:
    print("Tartibsiz")
"""
        #=====Q-16-misol=====#
"""
lst = [(), (), (), ('salom', 'najot'),('talim', 'x', 'a'),('m')]    
lst = [i for i in lst if i]
print(lst)
"""
