class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old


    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)


p = Person("Сергей", 20)
# p.set_old(35)
# p.__dict__["old"] = "old in object p"
# a = p.old
p.old = 35
del p.old
p.old = 5
print(p.__dict__)