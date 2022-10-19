"""
Template Method (comportamental) tem a intenção de definir um algoritmo em um método, postergando alguns passos para as subclasses por herança. Template method permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses utilizem caso necessário.add()

The Hollywood Principle: 'Don't call us, We'll Call you'
(IoC - Inversão de Controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self) -> None: 
        self.hook()
        self.operation_method_1()
        self.operation_method_2()
    
    def hook(self) -> None: pass
    
    @abstractmethod
    def operation_method_1(self) -> None: pass
    
    @abstractmethod
    def operation_method_2(self) -> None: pass


class ConcreteClass(Abstract):
    def hook(self) -> None:
        print('Estou utilizando o Hook')
        return super().hook()
    def operation_method_1(self) -> None: 
        print('Operação 1 concluida com sucesso')
    
    def operation_method_2(self) -> None: 
        print('Operação 2 concluida com sucesso')


if __name__ == '__main__':
    concrete = ConcreteClass()
    concrete.template_method()


