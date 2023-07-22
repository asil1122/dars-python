from os import system as sys
sys("cls")


class Card:
    def __init__(self, number, expire, password, type, balance, cvv = None):
        self.number = number
        self.expire = expire
        self.__password = password
        self.type = type
        self.__balance = balance
        self.__cvv = cvv
    
    def get_balance(self, code):
        if self.__password == code:
            return self.__balance
        return "Wrong password"

    def set_change_password(self, oldPassword: str, newPassword: str):
        if self.__password != oldPassword:
            raise KeyError("Eski parol noto'g'ri kiritildi")

        self.__password = newPassword
        return True

    def __str__(self):
        return f"""
type: {self.type}
number: {self.number[:2]+"** " + ("*" * 4 + " ") * 2 + self.number[-4:]}
expire: {self.expire}
password: {"*" * len(self.__password)}
balance: {self.__balance}
CVV: {self.__cvv or "Yo'q"}
"""



try:
    humo = Card("9860 1234 4589 2349", "09/27", "0000", "Humo", 2_000_000.0)
    visa = Card("4861 3456 8975 6465", "01/24", "0770", "UzCardVisa", 100_000, 990)

    humo.set_change_password("1200", "1234")
except Exception as message:
    print(message)