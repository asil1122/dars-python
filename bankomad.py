class Card:
    def __init__(self, seriya: str, muddati: str, turi: str, parol: str, price: float):
        self.seriya = seriya
        self.muddati = muddati
        self.turi = turi
        self.parol = parol
        self.price = price

    def parolniTekshirish(self, password: str) -> bool:
        if self.parol == password:
            return True
        return False

    def info(self):
        return f"""seriya: {self.seriya}
muddati: {self.muddati}
turi: {self.turi}
price: {self.price}
"""


class Bankomad:
    def __init__(self, bank_nomi: str, puli: float):
        self.bank_nomi = bank_nomi
        self.puli = puli
    
    def pulYechish(self, card: Card, password: str, price: float):
        if not card.parolniTekshirish(password):
            raise KeyError("Parol noto'g'ri")
        if card.price < price:
            raise KeyError("Summa Yetarli emas")
        if self.puli < price:
            raise KeyError("Bankomadda pul yetarli emas")
        
        card.price -= price
        return f"""yechilgan summa {price}\n"""


card = Card("8600 0120 5698 7845", "07/27", "UzCard", "3110", 1_000_000)
bankomad = Bankomad("SQB", 2_000_000)

print(card.info())
print(bankomad.pulYechish(card, "3110", 200_000))
print(card.info())