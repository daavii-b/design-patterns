"""
Flyweight é um padrão de projeto estrutural que tem a intenção de usar compartilhamento para suportar eficientemente grandes quantidades de objetos de forma granular.

Só use o Flyweight quandos TODAS as condições abaixos forem verdadeiras:

    - Uma aplicação utiliza uma grande quantidade de objetos;

    - Os custos de armazenamentos são altos por causa da grande quantidade de objetos;

    - A maioria dos estados de objetos podem se tornar extrínsecos;

    - Muitos objetos podem ser substituídos por poucos objetos compartilhados; 

    - A aplicação não depende da identidade dos objetos;

IMPORTANTE:
    
    - Estado intrinseco é o estado do objeto que não muda, esse estado deve estar dentro do objeto flyweight;

    - Estado extrínseco é o estado do objeto que muda, esse estado pode ser movido para fora do objeto flyweight;

DICIONÁRIO: 
    
    - Intrinseco -> que faz parte de ou que constitui a essência, a natureza de algo; que é próprio de algo; inerente;

    - Extrinseco - que não pertence a essência de algo; que é exterior;
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict

class Client:
    """ Context """
    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []
    
        # Extrinsic address data
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        self._addresses.append(address)
    
    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(
                self.address_number, self.address_details
            )


class Address:
    """ Flyweight """
    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code
    
    def show_address(self, address_number: str, address_details: str) -> None:
        print(
            f'{self._street} - {address_number} - {address_details} | {self._neighborhood} - {self._zip_code}'
        )

class AddressFactory:
    _addresses: Dict = {}

    @property
    def address_list(self) -> Dict:
        return self._addresses
    
    def _get_key(self, **kwargs) -> str:
        return ' - '.join(kwargs.values())
    
    def get_address(self, **kwargs) -> Address:
        _key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[_key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[_key] = address_flyweight
            print('Criando novo objeto')
        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    address = address_factory.get_address(street='Rua das Almas', neighborhood='Bairro da Paz', zip_code='80756-894')

    other_address = address_factory.get_address(street='Rua das Almas', neighborhood='Bairro da Paz', zip_code='80756-894')
    print('=='*25)

    client = Client('Daavi')
    client.address_number = '399'
    client.address_details = 'Ap 200 - 2'

    client.add_address(address)
    client.list_addresses()

    print('=='*25)
    
    client = Client('Jonas')
    client.address_number = '799'
    client.address_details = 'Ap 240 - 5'

    client.add_address(other_address)
    client.list_addresses()

