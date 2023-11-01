from abc import ABC, abstractmethod


# 抽象组件
class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

    def description(self):
        return "Unknown Beverage"


# 具体组件
class Coffee(Beverage):
    def cost(self):
        return 5.0

    def description(self):
        return "Coffee"


# 抽象装饰器
class CondimentDecorator(Beverage):
    pass


# 具体装饰器
class Sugar(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return 1.0 + self.beverage.cost()

    def description(self):
        return self.beverage.description() + ", Sugar"


class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def cost(self):
        return 2.0 + self.beverage.cost()

    def description(self):
        return self.beverage.description() + ", Milk"


# 客户端代码
coffee = Coffee()
print(coffee.description(), "$", coffee.cost())

coffee_with_sugar = Sugar(coffee)
print(coffee_with_sugar.description(), "$", coffee_with_sugar.cost())

coffee_with_sugar_and_milk = Milk(coffee_with_sugar)
print(coffee_with_sugar_and_milk.description(), "$", coffee_with_sugar_and_milk.cost())
