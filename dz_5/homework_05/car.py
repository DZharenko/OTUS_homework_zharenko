"""
Создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle


class Car(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, engine=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine):
        self.engine = engine








# класс Car должен быть наследником Vehicle
# добавьте атрибут engine классу Car
# объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
