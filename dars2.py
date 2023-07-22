
        #=====DARS-1=====#
"""
soz = list(map(str,input("Soz kiriting; ").split()))

for i in range(len(soz)):
    if soz[i].lower()[0] == "k":
        print(soz[i])
"""    
        #=====DARS-2=====#
"""
son = int(input("Son kiriting; "))
a = 1
for i in range(1 ,son + 1):
     a = a*i
print(a)
"""
        #=====DARS-3=====#
"""
son = int(input("Soz kiriting; "))
sonlar = [1,2,33,5,6,7,7]

for i in range(len(sonlar)):
    for j in range(len(sonlar)):
        if son==sonlar[i] + sonlar[j]:
            print(i,j,"indexlar")
"""