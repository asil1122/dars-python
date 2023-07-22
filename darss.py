        #=====dars-1=====#
"""
for a in range(100,1000):
    a = str(a)
    if a[0] == a[1] and a[0] !=a[2] or a[0] != a[1] and a[0] == a[2] or a[1]==a[2] and a[0] !=a[1]:
        print(int(a))
"""

        #=====dars-2=====#
"""
a = (input("son kiriting: "))

for i in a:
    print(int(i),end = " " )
"""
        #=====dars-3=====#
"""
lst = [123,456,789,852,12,42,61,369]

for i in range(len(lst)):
    if lst[i] % 2 == 0:
        print(lst[i],end = " ")
"""
        #=====dars-4=====#
"""
lst = [12,1,5,1,2,100]

lst.sort()
print(lst)
"""
        #=====dars-7=====#
"""
a = input("nimadur yoz; ")

a = a.split("/")
a.reverse()
print("".join(a))
"""