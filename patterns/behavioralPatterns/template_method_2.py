"""
Template Method (comportamental) tem a intenção de definir um algoritmo em um método, postergando alguns passos para as subclasses por herança. Template method permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses utilizem caso necessário.add()

The Hollywood Principle: 'Don't call us, We'll Call you'
(IoC - Inversão de Controle)
"""
from abc import ABC, abstractmethod
from typing import List, Tuple

class Pizza(ABC):
    """ Abstract Class"""
    def prepare(self) -> None:
        """ Template Method"""
        self.make_dough() # Abstract
        self.make_sauce() # Abstract
        self.make_pizza_body() # Abstract
        self.add_ingredients() # Abstract
        self.cook() # Abstract
        self.cut() # Concrete
        self.serve() # Concrete
    
    @abstractmethod
    def make_dough(self, ingredients: List[Tuple[str, str]]) -> None: pass
    @abstractmethod
    def make_sauce(self, ingredients: List[Tuple[str, str]]) -> None: pass
    @abstractmethod
    def make_pizza_body(self, size: str) -> None: pass
    @abstractmethod
    def add_ingredients(self, ingredients: List[Tuple[str, str]]) -> None: pass
    @abstractmethod
    def cook(self, timing: float, temperature: str) -> None: pass
    
    def cut(self) -> None:
        print('Cortando a Pizza de ', self.__class__.__name__)
    
    
    def serve(self) -> None:
        print('Servindo a Pizza de ', self.__class__.__name__)
    
    
class Calabreza(Pizza):
    def make_dough(self, ingredients: List[Tuple[str, str]]) -> None:
        print(f'Preparando a massa com [{ingredients}]')
    
    def make_sauce(self, ingredients: List[Tuple[str, str]]) -> None:
        print(f'Preparando o molho com [{ingredients}]')
    def make_pizza_body(self, size: str) -> None:
        print(f'Preparando a pizza de tamanho [{size}]')
    def add_ingredients(self, ingredients: List[Tuple[str, str]]) -> None:
        print(f'Adicionando os ingredientes [{ingredients}]')
    def cook(self, timing: float, temperature: str) -> None:
        print(f'Assando a Pizza. Tempo estimado: {timing} - Minutos - Temperatura: {temperature}')    


if __name__ == '__main__':
    pizza = Calabreza()
    