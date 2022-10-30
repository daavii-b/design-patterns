"""

Composite é um padrão de projeto estrutural que permite que você utilize a composição para criar objetos em estruturas de árvores. O padrão permite os clientes tratarem de maneira uniforme objetos individuais (Leaf) e composições de objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa ser representada em formato hierárquico (árvore).

No padrão composite, temoa dois tipos de objetos:
    - Composite (que representa nós internos da árvore) e Leaf (que representa nós externos da árvore).


  -  Objetos Composite são objetos mais complexos e com filhos.
        - Geralmente, eles delegam trabalho para os filhos usando um método em comum.

  - Objetos Leaf são objetos simples, da ponta e sem filhos.
        - Geralmente, são esses objetos que realizam trabalho real da aplicação.

"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class IBoxStructure(ABC):
    """ BoxStructure Interface | Composite """
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass
    
    def add(self, child: IBoxStructure) -> None: pass

    def remove(self, child: IBoxStructure) -> None: pass

class Box(IBoxStructure):
    """ Composite """
    
    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[IBoxStructure] = []

    def print_content(self) -> None:
        print(f'{self.name}:\n')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum(
            [child.get_price() for child in self._children]
        )
    
    def add(self, child: IBoxStructure) -> Box:
        self._children.append(child)
        return self
        
    def remove(self, child: IBoxStructure) -> Box:
        self._children.remove(child) if child in self._children else ... 
        return self


class Product(IBoxStructure):
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
        
    def print_content(self) -> None:
        print(f'\t{self.name} - {self.price}')
        
    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    # Leaf
    camiseta_azul = Product('Camiseta Azul', 92.2)
    camiseta_vermelho = Product('Camiseta Vermelho', 28.2)
    camiseta_verde = Product('Camiseta Verde', 52.2)

    
    # Composite
    caixa_de_camisetas = Box('Caixa de camisas')

    caixa_de_camisetas.add(camiseta_azul).add(camiseta_vermelho).add(camiseta_verde)

    caixa_de_camisetas.print_content()

    print('='*30)
    
    # Leaf
    smartphone = Product('Smartphone', 4500)
    iphone = Product('Iphone', 9500)

    # Composite

    caixa_de_smartphones = Box('Caixa de Smartphone')

    caixa_de_smartphones.add(smartphone).add(iphone)

    caixa_de_smartphones.print_content()

    print('='*30)

    # Composite
    pedido = Box('Pedidos')
    pedido.add(caixa_de_smartphones).add(caixa_de_camisetas)
    
    pedido.print_content()
    print('\nPreco Total do Pedido: ', pedido.get_price())