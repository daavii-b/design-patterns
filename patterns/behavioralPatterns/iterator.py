"""
Iterator é um padrão comportamental que tem a intenção de fornecer um meio de acessar,
sequenciamente, os elementos de um objeto agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar seus elementos sem expor sua estrutura interna.

- Uma coleção pode ter maneiras e percursos diferentes para expor seus elementos.

-Você deve separar a complexidade dos algoritmos de iteração da coleção em si.


A idéia principal do padrão é retirar a responsabilidade de  acesso e percurso de uma coleção, delegando tais tarefas para um objeto iterador.
"""

from collections.abc import Iterator, Iterable
from  typing import List, Any


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0
        
    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1
        
    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration
        
class MyList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._iterator: Iterator = MyIterator(self._items)
    
    def add(self, value: Any) -> None:
        self._items.append(value)
        
    def __iter__(self) -> Iterator:
        return self._iterator
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} -> {self._items}'
    
    def __repr__(self) -> str:
        return self.__str__()

class ReverseList(Iterable):
    def __init__(self) -> None:
        self._items: List[Any] = []
        self._iterator: Iterator = MyIterator(self._items)
    
    def add(self, value: Any) -> None:
        self._items.append(value)
        
    def __iter__(self) -> Iterator:
        return self._iterator
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__} -> {self._items}'
    
    def __repr__(self) -> str:
        return self.__str__()


if __name__ == '__main__':
    my_list = MyList()
    my_list.add('Test')
    my_list.add('Ana')
    my_list.add('Otávio')

    print(my_list)

    for item in my_list:
        print(item)

    reverse_list = ReverseList()
    reverse_list.add('Test')
    reverse_list.add('Ana')
    reverse_list.add('Otávio')

    print(reverse_list)

    for item in reverse_list:
        print(item)