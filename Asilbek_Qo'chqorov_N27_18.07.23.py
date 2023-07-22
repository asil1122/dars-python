        #=====2-MISOL=====#

# class Mashina:
#     def __init__(self, nomi=str, turi=str, yilli=int, narxi=4000):
#         self.nomi = nomi
#         self.turi = turi
#         self.narxi  = narxi
#         self.yilli = yilli

#     def info(self):
#         return f"""
# Nomi: {self.nomi}
# Turi: {self.turi}
# Narxi: {self.narxi}
# Yilli: {self.yilli}"""


# car = Mashina("Gentra","Yegil avtomabil",2022,18000)
# car1 = Mashina("Treker 2","Yengil avtomabile",2023,25000)
# car2 = Mashina("Labo","Yuk avtomabil",2020,11000)
# car3 = Mashina("KIA K5","Yengil avtomabile",2021,38000)
# lst = [car, car1, car2, car3]
# lst.sort(key=lambda x: x.yilli)
# for i in range(len(lst)):
#     print(lst[i].info())

        #=====3-MISOL=====#

# class Countries:
#     def __init__(self,davlat_nomi, poytahti, axoli_soni, yer_maydoni, prezidenti):
#         self.davlat = davlat_nomi
#         self.poytaht = poytahti
#         self.axoli = axoli_soni
#         self.maydon = yer_maydoni
#         self.prizident = prezidenti

#     def info(self):
#         return f"""
# Davlat nomi: {self.davlat}
# Poytahti: {self.poytaht}
# Axolis soni: {self.axoli}
# Yer maydoni: {self.maydon}
# Prezidenti: {self.prizident}"""


# lst = []
# for i in range(2):
#     Countrie = Countries(input("Davlatni kiriting: "),input("Poytahtini kiriting: "),int(input("Axoli sonini kiriting: ")),int(input("Yer maydoni: ")),input("Prezidenti kim?: "))
#     print("")
#     lst.append(Countrie)
# lst.sort(key=lambda x: x.davlat)
# for i in range(len(lst)):
#     print(lst[i].info())