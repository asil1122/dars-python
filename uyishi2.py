        #=====R1-MISOL=====#
"""
sample_set={"Asil","Johon","Sarvar"}
sample_list=["Shaxs","nimadur","kimdur"]
sample_list=set(sample_list)
sample_set.update(sample_list)
print(sample_set)
"""
        #=====R2-MISOL=====#
"""
set={10,20,30,40,50}
set2={30,40,50,60,70}
sett=set.intersection(set2)
print(sett)
"""
        #=====R3-MISOL=====#
"""
set={10,20,30,40,50}
set2={30,40,50,60,70}
set.update(set2)
print(set)
"""
        #=====R4-MISOL=====#
"""
kalit=['ten','twenty','thirty']
value=[10,20,30]
a = dict(zip(kalit, value))
print(a)
"""
        #=====R6-MISOL=====#
"""
Dict={'a':100,'b':200,'c':300}
a=list(Dict.values())
for i in range(len(a)):
    if a[i]==200:
      print("True")
else:
    print("False") 
"""
        #=====R7-MISOL=====#
"""
sampleDict={
    "name":"Asilbek",
    "age":"16",
    "salary":100000000,
    "city":"TASHKENT"
}
a=list(sampleDict.keys())
a2=list(sampleDict.values())
a[3]='Location'
sampleDict=dict(zip(a,a2))
print(sampleDict)
"""
        #=====R8-MISOL=====#
"""
list = [
     [1, 'Asil', 'V'],
     [2, 'Hurshid', 'V'],
     [3, 'Behruz', 'VI'],
     [4, 'Erkin', 'VI'],
     [5, 'Adham', 'VII']
]
dict={}
for i in list:
    dict[i[0]]=[i[1],i[2]]
print(dict)
"""


        #=====1-MASALA=====#
"""
lst=[(1,2),(2,3),(3,4)]
for i in range(len(lst)):
    lst[i]=list(lst[i])
print(lst)
"""
        #=====2-MASALA=====#
"""
lst=[(5,5),(4,4),(3,3)]
for i in range(len(lst)):
    lst[i]=list(lst[i])
for i in range(len(lst)):
    lst[i]=lst[i][0] + lst[i][1]
print(lst)
"""
