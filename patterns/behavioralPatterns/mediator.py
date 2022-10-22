"""
Mediator é um padrão comportamental que tem a intenção de definir um objeto que encapsula a forma como um conjunto de objetos interage . O Mediator promove o baixo acoplamento ao evitar que os objetos se refiram uns aos outros explicitamente e permite variar suas interações independentemente.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List



class Colleague(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
    
    @abstractmethod
    def broadcast(self, message: str) -> None: pass


    @abstractmethod
    def direct(self, message: str) -> None: pass

class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self._name = name
        self._mediator = mediator
   
    def broadcast(self, message: str) -> None: 
        self._mediator.broadcast(self, message)
    def direct(self, receiver: str,  message: str) -> None:
        self._mediator.direct(self, receiver, message)
class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, message: str) -> None: pass
    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, message: str) -> None: pass

class ChatRoom(Mediator):
    def __init__(self) -> None:
        self._colleagues: List[Colleague] = []
    
    def _is_colleague(self, colleague: Colleague) -> None:
        return colleague in self._colleagues

    def add(self, colleague: Colleague) -> None:
        if not self._is_colleague(colleague):
            self._colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self._is_colleague(colleague):
            self._colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, message: str) -> None: 
        if not self._is_colleague(colleague):
            return
        print(f'Global -> {colleague._name}: {message.capitalize()} ')

    def direct(self, sender: Colleague, receiver: str, message: str) -> None:
        if not self._is_colleague(sender):
            return
        try:
            receiver: List[Colleague] = [
                colleague for colleague in self._colleagues
                if colleague._name == receiver
            ][0]
        except IndexError:
            return        
        
        print(
            f'Direct -> {sender._name} enviou uma mensagem para {receiver._name}: {message.capitalize()}'
        )


if __name__ == '__main__':
    chat = ChatRoom()
    
    davi = Person('Daavi', chat)
    luiz = Person('Luiz', chat)
    leo = Person('Leo', chat)
    carlos = Person('Carlos', chat)

    chat.add(davi)
    chat.add(luiz)
    chat.add(leo)
    chat.add(carlos)
    
    davi.broadcast('Minha messagem para testar')
    luiz.broadcast('Outra mensagem, so que diferente para testar')
    leo.direct('Carlos', 'Ola Carlos, sou eu, Leo.')

    chat.remove(carlos)

    leo.direct('Carlos', 'Ola Carlos, sou eu, Leo.')
    
    davi.direct('Leo', 'Oláaa')
    leo.direct('Luiz', 'Oláaa')
    luiz.broadcast('Olllaaaaa')