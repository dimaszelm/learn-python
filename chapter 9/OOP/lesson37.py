from dataclasses import dataclass, field
from pprint import pprint


class Thing:
    def __init__(self, name, weigh, price, dims = []):
        self.name = name
        self.weight = weigh
        self.price = price
        self.dims = dims

    def __repr__(self):
        return f"Thing: {self.__dict__}"


@dataclass
class ThingData:
    name: str
    #price: float = 0 - так делать нельзя, значения по умолчанию всегда должны быть последними.
    weight: int = 0
    price: float = 0
    #dims: list = [] - нельзя изменяемые объекты, нужно использовать функцию ниже.
    dims: list = field(default_factory= list)


#__init__(), __repr__(), __eq__() - можем переопределять любой метод.
    # def __eq__(self, other):
    #     return self.weight == other.weight

# td = ThingData("ученик по Python", 100, 512)
# td_2 =ThingData("Python ООП2", 80, 1000)
# td_3 = ThingData("Python ООП", 80, 512)
# print(td_3 == td_2)
# pprint(ThingData.__dict__)
# t = Thing("ученик по Python", 100, 1024)
# t.dims.append(10)
td = ThingData("ученик по Python", 100, 1024)
td.dims.append(10)
td2 = ThingData("ученик по Python", 100, 1024)
print(td2)
