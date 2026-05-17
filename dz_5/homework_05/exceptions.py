"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class CarError(Exception):
    pass

class LowFuelError(CarError):
    pass

class NotEnoughFuel(CarError):
    pass

class CargoOverload(CarError):
    pass




