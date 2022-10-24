"""
O proxy é um padrão de projeto estrutural que tem a intenção de fornecer um objeto substituto que atua como se fosse o objeto real que o código cliente gostaria de usar.

O proxy receberá as solicitações e terá controle sobre como e quando repassar tais solicitações ao objeto real.

Com base no modo como proxies são usados, nós os classificamos como:

    - Proxy Virtual: controla acesso a recursos que podem ser caros para a criação ou utilização.

    - Proxy Remoto: controla acesso a recursos que estão em servidores remotos.

    - Proxy de Proteção: controla acesso a recursos que possam necessitar autenticação ou permissão.

    - Proxy Inteligente: além de controlar o acesso ao objeto real, também executa tarefas adicionais para saber quando e como executar determinadas ações.

    Proxies podem fazer várias coisas diferentes:
        criar logs, autenticar usuários, distribuir serviços, criar cache, criar e destruir objetos, adiar execuções e muito mais...
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict

class IUser(ABC):
    """ User Interface """
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_user_data(self) -> Dict: pass


class User(IUser):
    
    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2) # Simulando uma requisição
        self.firstname = firstname
        self.lastname = lastname
    
    def get_addresses(self) -> List[Dict]:
        sleep(2) # Simulando uma requisição
        return [
            {'rua': 'Rua das Flores', 'numero': 234}
        ]

    def get_user_data(self) -> Dict:
        sleep(2) # Simulando uma requisição
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'addresses': self.get_addresses(),
            'CPF': '123.456.789-10',
        }

class UserProxy(IUser):

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self._user: User 
        self._cached_addresses: List[Dict]
        self._user_data: Dict
        
    def get_user(self) -> None:
        if not hasattr(self, '_user'):
            self._user = User(self.firstname, self.lastname)
            
    def get_addresses(self) -> List[Dict]:
        if not hasattr(self, '_cached_addresses'):
            self.get_user()
            self._cached_addresses = self._user.get_addresses()
        return self._cached_addresses
        
    def get_user_data(self) -> Dict:
        if not hasattr(self, '_user_data'):
            self.get_user()
            self._user_data = self._user.get_user_data()
        return self._user_data

if __name__ == '__main__':
    user = UserProxy('Daavii', 'Briito')
    print(user.firstname)
    print(user.lastname)

    # No Chached Data | Slowly execution
    user_data = user.get_user_data()
    user_addresses = user.get_addresses()
    
    print(f'User Data -> {user_data}')
    print(f'User Addresses -> {user_addresses}')

    user_data = user.get_user_data()
    user_addresses = user.get_addresses()

    #  Cached Data | Quickly Execution
    print(f'User Data in Cache -> {user_data}')
    print(f'User Addresses in Cache-> {user_addresses}')
