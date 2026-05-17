"""
Создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle

from homework_05 import exceptions


class Plane(Vehicle):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo = 0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo <= self.max_cargo:
            self.cargo += new_cargo
        else:
            raise exceptions.CargoOverload('Ошибка. Машина перегружена')

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
