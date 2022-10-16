"""
Abstract Factory é um padrão de criação que fornece uma interface para criar familias  de objetos relacionados ou dependetes sem especificar suas classes concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods para criar objetos. 


Uma diferença importante entre Factory Method e Abstract Factory é que o Factory Method usa herança, enquanto Abstract Factory usa a composição.

Principio: programe para interfaces, e não para implementações.
"""

from abc import ABC, abstractmethod


class LuxuryVehicle(ABC): 
    @abstractmethod
    def get_client(self) -> None:
        pass
class PopularVehicle(ABC): 
    @abstractmethod
    def get_client(self) -> None:
        pass


class LuxuryCarNZ(LuxuryVehicle):
    def get_client(self) -> None:
        print('Carro de luxo ZN buscando cliente no local desejado')


class PopularCarNZ(PopularVehicle):
    def get_client(self) -> None:
        print('Carro popular ZN buscando cliente no local desejado')

class LuxuryCarSZ(LuxuryVehicle):
    def get_client(self) -> None:
        print('Carro de luxo S N buscando cliente no local desejado')


class PopularCarSZ(PopularVehicle):
    def get_client(self) -> None:
        print('Carro popular S N buscando cliente no local desejado')


class VehicleFactory(ABC):    
    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVehicle: pass    
    @staticmethod
    @abstractmethod
    def get_popular_car() -> PopularVehicle: pass    
     

class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarNZ()
            
    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarNZ()    
        
class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarSZ()
    
    @staticmethod
    def get_popular_car() -> PopularVehicle:    
        return PopularCarSZ()


class Affiliate:
    def get_clients(self):
        for factory in [NorthZoneVehicleFactory(), SouthZoneVehicleFactory()]:
            luxury_car = factory.get_luxury_car()
            luxury_car.get_client()

            popular_car = factory.get_popular_car()
            popular_car.get_client()

if __name__ == '__main__':
    affiliate = Affiliate()
    affiliate.get_clients()