from abc import *
from math import *

class Calculator:
    def __init__(self, son):
        self.__son = son

    @abstractmethod
    def set_plus(self, son=1):
        self.__son = self.__son + son

    @abstractmethod
    def set_minus(self, son=1):
        self.__son = self.__son - son

    @abstractmethod
    def set_multiply(self, son=2):
        self.__son = self.__son * son

    @abstractmethod
    def set_mod(self,son):
        self.__son = self.__son %son

    @abstractmethod
    def set_pow(self, son):
        self.__son = self.__son **son

    @abstractmethod
    def set_divide(self, son):
        self.__son = self.__son / son

    @abstractmethod
    def set_sqrt(self):
        self.__son = sqrt(self.__son)
    try:
        def N(self):
            raise NameError("Xato qilding")
    except Exception as arr:
        print(arr)

    def get_answer(self):
        return f"N ning qiymati-{self.__son}"

class Mat(Calculator):

    def set_plus(self, son=1):
        super().set_plus(son)

    def set_minus(self, son=1):
        super().set_minus(son)

    def set_multiply(self, son=2):
        super().set_multiply(son)

    def set_mod(self, son):
        super().set_mod(son)

    def set_pow(self, son):
        super().set_pow(son)

    def set_divide(self, son):
        super().set_divide(son)

    def set_sqrt(self):
        super().set_sqrt()

    def N(self):
        super().N()

    def get_answer(self):
        return super().get_answer()


calc = Mat(10)
print(calc.get_answer())
calc.set_plus(5)
print(calc.get_answer())
calc.set_plus()
print(calc.get_answer())
calc.set_mod(2)
print(calc.get_answer())
calc.set_plus()
print(calc.get_answer())
calc.set_multiply(100)
print(calc.get_answer())
calc.set_multiply()
print(calc.get_answer())
calc.set_minus(40)
print(calc.get_answer())
calc.set_minus()
print(calc.get_answer())
calc.N()