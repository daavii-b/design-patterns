"""
Factory Method é um padrão de criação que permite definir uma interface para criar objetos, mas deixa as subclasses decidirem quaus objetos criar. O Factory Method permite adiar a instanciação para as subclasses, garantindo, o baixo acoplamento de classes.

"""

from abc import ABC, abstractmethod


class Vehicle(ABC): 
    @abstractmethod
    def get_client(self) -> None:
        pass


class CarroLuxo(Vehicle):
    def get_client(self) -> None:
        print('Carro de luxo buscando cliente no local desejado')


class CarroPopular(Vehicle):
    def get_client(self) -> None:
        print('Carro popular buscando cliente no local desejado')


class VehicleFactory(ABC):
    def __init__(self, type: str) -> None:
        self.car = self.get_car(type)
    
    @staticmethod
    @abstractmethod
    def get_car(type: str, ) -> Vehicle: pass    
    
    def get_client(self) -> None:
        self.car.get_client()


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_car(type: str, ) -> Vehicle:
        if type == 'luxo':
            return CarroLuxo()
        elif type == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'
        
class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_car(type: str, ) -> Vehicle:
        if type == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'



if __name__ == '__main__':
    from random import choice
    north_available_vehicle = ['luxo', 'popular']
    south_available_vehicle = ['popular', ]
    print('Zona Norte')
    for i in range(10):
        vehicle = NorthZoneVehicleFactory(choice(north_available_vehicle))
        vehicle.get_client() 
    
    print('Zona Sul')
    for i in range(10):
        vehicle = SouthZoneVehicleFactory(choice(south_available_vehicle))
        vehicle.get_client() 