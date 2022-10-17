"""
Builder é um padrão de criação que tem a intenção de separar a construção de um objeto complexo de sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo e isso já é possivel no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos (method chaining).
"""

from abc import ABC, abstractmethod

class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__()



class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firstname(self, firstname: str): pass

    @abstractmethod
    def add_lastname(self, lastname: str): pass

    @abstractmethod
    def add_phone_number(self, phone_number: int): pass

    @abstractmethod
    def add_age(self, age: int): pass

    @abstractmethod
    def add_address(self, address: str): pass


class UserBuilder(IUserBuilder):

    def __init__(self) -> None:
        self.reset()
    
    def reset(self) -> None:
        self._result = User()
    
    @property
    def result(self) -> object:
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname: str) -> None:
        self._result.firstname = firstname
        return self
    
    def add_lastname(self, lastname: str) -> None:
        self._result.lastname = lastname
        return self

    def add_phone_number(self, phone_number: int) -> None: 
        self._result.phone_numbers.append(phone_number)
        return self

    def add_age(self, age: int) -> None: 
        self._result.age = age
        return self

    def add_address(self, address: str) -> None: 
        self._result.addresses.append(address)
        return self

 
class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder
    
    def with_age(self, firstname: str, lastname: str, age: int):
        self._builder.add_firstname(firstname).add_lastname(lastname).add_age(age)
        return self._builder.result


    def with_address(self, firstname: str, lastname: str, age: int, address: str):
        self._builder.add_firstname(firstname)
        self._builder.add_lastname(lastname)
        self._builder.add_age(age)
        self._builder.add_address(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user = user_director.with_age('Davi', 'Brito', 22)
    user = user_director.with_address('Davi', 'Brito', 22, 'Rua Desembargador 33')

    print(user)