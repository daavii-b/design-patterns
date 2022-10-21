"""
Chain of Responsibility (COR) é um padrão comportamental que tem a intenção de evitar o acoplamento de umsa solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitação. 
Encadear objetos receptores passando a solicitação ao longo da cadeia até que um objeto a trate.
"""

# Implementando com class

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass

class HandlerABC(Handler):
    def __init__(self, sucessor: Handler):
        self.letters: list = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__}, conseguiu tratar o valor da {letter}'
        return self.sucessor.handle(letter)

class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler):
        self.letters: list = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__}, conseguiu tratar o valor da {letter}'
        return self.sucessor.handle(letter)

class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'{self.__class__.__name__}, não conseguiu tratar o valor da {letter}'

if __name__ == '__main__':
    handler = HandlerABC(HandlerDEF(HandlerUnsolved()))
    print(handler.handle('A'))
    print(handler.handle('B'))
    print(handler.handle('D'))
    print(handler.handle('F'))
    print(handler.handle('R'))
    print(handler.handle('T'))
    print(handler.handle('I'))