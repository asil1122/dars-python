from os import system
system("cls")
        #=====1-MASALA=====# 
# class kitob:
#     def __init__(self,nomi: str, mualliflari: str,narxi: int, nashriyoti: str):
#         self.nomi = nomi
#         self.mualliflari = mualliflari
#         self.narxi = narxi
#         self.nashriyoti = nashriyoti

#     def malumot(self):
#        if self.nashriyoti[0].lower() >= 'a' and self.nashriyoti[0].lower() <= 'h':
#         print(f"""narxi: {self.narxi} usz,
# nashriyoti: {self.nashriyoti},
# muallifi: {self.mualliflari},
# kitob nomi: {self.nomi}""")
#         print()

# kitob1 = kitob("Asilning sayohati","Hurshid Eshmatov",1_000_000,"Asil nashiryoti")
# kitob2 = kitob("Bir kunli bayram","Sarvar Abzalxonov",500_000,"O'z nashiryoti")
# kitob3 = kitob("Millioner bola","Erkin Yusupov",1_000_000,"Gazeta nashiryoti")
# kitob4 = kitob("Bir kunda million","Azizbek Mamasoliyev",1_000_000,"Mahalla nashiryoti")

# kitob1.malumot()
# kitob2.malumot()
# kitob3.malumot()
# kitob4.malumot()

        #=====2-MASALA=====#
# class Kompyuter:
#     def __init__(self,nomi:str, RAMI:int, narxi:int,protsessori:str):
#         self.nomi = nomi
#         self.RAMI = RAMI
#         self.narxi = narxi
#         self.protsessori = protsessori
#     def info(self):
#         if self.RAMI >= 4 and self.RAMI <= 16:
#             print(f"""nomi: {self.nomi},
# RAMI: {self.RAMI},
# narxi: {self.narxi},
# protsessori: {self.protsessori}""")
#         print()

# komputer1 = Kompyuter("Victus",8,8_000_000,"intel")
# komputer2 = Kompyuter("Acer",4,6_000_000,"intel")
# komputer3 = Kompyuter("Hp",2,5_500_000,"intel")
# komputer4 = Kompyuter("Macbook",16,12_000_000,"mac os")

# komputer1.info()
# komputer2.info()
# komputer3.info()
# komputer4.info()

        #=====3-MASALA=====#
# class Foydalanuvchi:
#     def __init__(self,name: str=input("Ismingizni kiriting: "), surname: str=input("Familyangizni kiriting: "), email: str=input("Emailingizni kiriting: "),device: str=input("Qurulmangizni kiriting: ")):
#         self.ism = name
#         self.familya = surname
#         self.email = email
#         self.qurulma = device
#     def malumot(self):
#         print()
#         print(f"""Foydalanuvchining: ismi: {self.ism},
# familyasi: {self.familya},
# emaili: {self.email},
# telefon qurulmasi: {self.qurulma}""")

# user = Foydalanuvchi()
# user.malumot()
