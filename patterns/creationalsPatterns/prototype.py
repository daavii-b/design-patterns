"""
O Prototype é usado para especificar os tipos de objetos a serem criados usando uma instância-prototipo e criar novos objetos pela cópia desse prototipo.
"""
from __future__ import annotations
from copy import deepcopy 
from typing import List

class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__()        


class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street 
        self.number = number
        self.address: str = f'{street} - {number}'


class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname 
        self.lastname = lastname
        self.addresses: List[Address] = list()

    
    def add_address(self, address: Address) -> None:
        self.addresses.append(address)
    
    def clone(self) -> Person:
        return deepcopy(self)
if __name__ == '__main__':
    person = Person('Davi', 'Brito')
    address = Address('Rua do Limoeiro', '24')
    person.add_address(address)

    other_person = person.clone()
    other_person.firstname = 'Ana'
    other_person.lastname = 'Araújo'

    print(person)
    print(other_person)