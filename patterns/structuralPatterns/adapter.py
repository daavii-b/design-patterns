"""
Adapter é um padrão de projeto estrutural que tem a intenção de permitir que duas classes que seriam incompativeis trabalhem em conjunto através de um 'adaptador'.
"""

from abc import  ABC, abstractmethod

class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass
    
    @abstractmethod
    def bottom(self) -> None: pass
    
    @abstractmethod
    def right(self) -> None: pass
    
    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    def top(self) -> None:
        print('Control -> Movendo para cima...')
    
    def bottom(self) -> None:
        print('Control -> Movendo para baixo...')

    def right(self) -> None:
        print('Control -> Movendo para direita...')

    
    def left(self) -> None:
        print('Control -> Movendo para esquerda...')

class NewControl:
    def move_top(self) -> None:
        print('NewControl -> Movendo para cima...')
    
    def move_bottom(self) -> None:
        print('NewControl -> Movendo para baixo...')

    def move_right(self) -> None:
        print('NewControl -> Movendo para direita...')

    
    def move_left(self) -> None:
        print('NewControl -> Movendo para esquerda...')


class ControlAdapter:
    """ Adapter Object """
    def __init__(self, control: NewControl):
        self.control = control
    
    def top(self) -> None:
        self.control.move_top()
    
    def bottom(self) -> None:
        self.control.move_bottom()

    def right(self) -> None:
        self.control.move_right()

    
    def left(self) -> None:
        self.control.move_left()

class ControlAdapter2(Control, NewControl):
    """ Adapter class """    
    def top(self) -> None:
        self.move_top()
    
    def bottom(self) -> None:
        self.move_bottom()

    def right(self) -> None:
        self.move_right()

    
    def left(self) -> None:
        self.move_left()


if __name__ == '__main__':
    print('Concrete Control. \n')
    control = Control()
    
    control.top()
    control.bottom()
    control.right()
    control.left()

    print('-=-'*30)
    # Control With Adapter Object
    print('Using a new control with Adapter Object. \n')
    control_object = ControlAdapter(NewControl())

    control_object.top()
    control_object.bottom()
    control_object.right()
    control_object.left()

    print('-=-'*30)
    # Control With Adapter Class
    print('Using a new control with Adapter Class. \n')
    control_class = ControlAdapter2()
    
    control_class.top()
    control_class.bottom()
    control_class.right()
    control_class.left()

    print('-=-'*30)
