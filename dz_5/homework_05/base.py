"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05 import exceptions


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):

        if self.started:
            print('Двигатель уже запущен')
            return

        if self.fuel > 0:
            self.started = True
        else:
            raise exceptions.LowFuelError('Нет топлива. Машина не завелась.')

    def move(self, distance):
        if distance <= (self.fuel/self.fuel_consumption)*100:
            self.fuel -= distance / 100 * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel('Недостаточно топлива для поездки')







