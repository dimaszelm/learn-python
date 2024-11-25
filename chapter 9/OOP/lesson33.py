class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + "@" + psw)

    class Meta:
        ordering = ["id"]
        #t = Women.title - нельзя. во вложеных классах обращаться к атрибутам внешнего класса нельзя! потому что еще не отработал инициализатор и класс women не создан
        def __init__(self, acces):
            self._acces = acces
            # self._t = Women.title - можно, но так делать не стоит.




w = Women("root", "12345")
# print(w.ordering)
# print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)