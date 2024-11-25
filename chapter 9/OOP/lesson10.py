from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзийклмнопрстуфхцчшщбыъэюя-"
    S_RUS_UPPER = S_RUS.upper()
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        # self.verify_old(old)
        # self.verify_ps(ps)
        # self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight


    @classmethod
    def verify_fio(cls,fio):
        if type(fio) != str:
            raise TypeError("Фио должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("в фио должен быть хотябы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В фио можно использовать только буквенные символы и дефиз")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне от 14 до 120")

    @classmethod
    def verify_weight(cls, w):
        if type(w) != int or w < 14 or w > 120:
            raise TypeError("вес должен быть от 20 и выше")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError(" паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Ссерия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self,old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps





p = Person("Балакирев Сергей Михайлович", 38, "1234 567890", 80)
p.old = 100
p.passport = "4567 123456"
p.weight = 70
print(p.__dict__)