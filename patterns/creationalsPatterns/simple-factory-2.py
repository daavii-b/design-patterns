#   Na programação POO, o termo factory, é usado para descrever classes ou métodos que são responsaveis por criar objetos.


"""
Caso de Uso do Pattern:
    Supondo que estamos 'criando' o app da Uber.
    
    Identificamos que o cliente precisa de um veículo para se locomover.
"""

from abc import ABC, abstractmethod


class Veiculo(ABC): 
    @abstractmethod
    def get_client(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def get_client(self) -> None:
        print('Carro de luxo buscando cliente no local desejado')


class CarroPopular(Veiculo):
    def get_client(self) -> None:
        print('Carro popular buscando cliente no local desejado')


class VeiculoFactory:
    def __init__(self, type: str) -> None:
        self.car = self.get_car(type)
    
    @staticmethod
    def get_car(type: str, ) -> Veiculo:
        if type == 'luxo':
            return CarroLuxo()
        elif type == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não existe'
    
    def get_client(self) -> None:
        self.car.get_client()
    
if __name__ == '__main__':
    from random import choice
    available_cars = ['luxo', 'popular']

    for i in range(10):
        carro = VeiculoFactory(choice(available_cars))
        carro.get_client()