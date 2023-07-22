        #=====1-MASALA=====#

# import random
# class MyList(list):
#     def random(self, n, max, min):
#         for i in range(n):
#             self.append(random.randint(min, max))
#         return lst


# lst = MyList()
# print(lst.random(int(input("Uzunlikni kiriting: ")), 100, -100))

        #=====MASALANI-1=====#
# class Soldat:
#     def __init__(self):
#         self.yosh = int(input("Yoshini kiriting: "))
#         self.vazn = int(input("Vaznini kiriting: "))
#         self.boy = int(input("Bo'yini kiriting: "))
#         self.jinsi = input("Jinsini kiriting: ")

# class Armiya(Soldat):
#     pass
#     def malumotnoma(self):
#         return f"""Yoshi-{self.yosh}
# Jinsi-{self.jinsi}
# Bo'yi-{self.boy}
# Vazni-{self.vazn}"""

# A1 = Armiya()
# print(A1.malumotnoma())
# lst = [A1]
# for i in lst:
#     if i.jinsi.lower() == "erkak" and i.yosh > 18:
#         pass
#         if i.boy <150 and i.vazn < 75:
#             print(i.malumotnoma())
#             print("Piyoda qo'shini: ")
#         elif i.boy >150 and i.vazn > 75:
#             print(i.malumotnoma())
#             print("Tank qo'shini: ")

        #=====U4-1-MASALA=====#
# class Mashina:
#     def __init__(self, Brand, Model, Color):
#         self.brand = Brand
#         self.model = Model
#         self.color = Color

#     def get_malumot(self):
#         return f"""
# Nomi: {self.brand}
# Madeli: {self.model}
# Rangi: {self.color}
# """
#     def set_Change(self):
#         self.brand = input("Qanday brandga alishtirasiz: ")
#         self.model = input("Qanday madelga alishtirasiz: ")
#         self.color = input("Qanday ranga alishtirasiz: ")

#     def malumot(self):
#             return f"""\n
#     Noni: {self.brand}
#     Madeli: {self.model}
#     Rangi: {self.color}
#     """

# car = Mashina("Gentra","1,5", "qora")
# print(car.get_malumot())
# car.set_Change()
# print(car.malumot())
