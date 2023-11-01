from abc import ABC, abstractmethod


# 汉堡建造者接口
class BurgerBuilder(ABC):
    def __init__(self):
        self.burger = Burger()

    @abstractmethod
    def set_bread(self):
        pass

    @abstractmethod
    def set_condiments(self):
        pass

    @abstractmethod
    def set_fillings(self):
        pass

    def get_burger(self):
        return self.burger


class VeganBurgerBuilder(BurgerBuilder):
    def set_bread(self):
        self.burger.bread = "Whole grain bread"

    def set_condiments(self):
        self.burger.condiments = "Vegan mayo and mustard"

    def set_fillings(self):
        self.burger.fillings = "Lettuce, tomato, and vegan patty"


class CheeseBurgerBuilder(BurgerBuilder):
    def set_bread(self):
        self.burger.bread = "White bread"

    def set_condiments(self):
        self.burger.condiments = "Mayo, ketchup, and mustard"

    def set_fillings(self):
        self.burger.fillings = "Lettuce, tomato, patty, and cheese"


# 汉堡产品
class Burger:
    def __init__(self, bread="", condiments="", fillings=""):
        self.bread = bread
        self.condiments = condiments
        self.fillings = fillings

    def __str__(self):
        return f"{self.bread} burger with {self.fillings} and {self.condiments}"


# 指导者
class Chef:
    def prepare_burger(self, builder):
        builder.set_bread()
        builder.set_condiments()
        builder.set_fillings()
        return builder.get_burger()


# 客户端代码
chef = Chef()

vegan_burger_builder = VeganBurgerBuilder()
vegan_burger = chef.prepare_burger(vegan_burger_builder)
print(vegan_burger)

cheese_burger_builder = CheeseBurgerBuilder()
cheese_burger = chef.prepare_burger(cheese_burger_builder)
print(cheese_burger)
