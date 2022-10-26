"""
Bridge é um padrão de projeto estrutural que tem a intenção de desacoplar uma abstração da sua implementação, de modo que as duas possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho por conta própria, ela delega parte ou todo o trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto estrutural que tem a intenção de permitir que duas classes que seriam incompativeis trabalhem em conjunto através de um 'adaptador'.


Diferença (GOF pag. 208) - A diferença chave entre esses padrões está na suas intenções... O padrão Adapter faz as coisas funcionarem APÓS elas terem sidos projetadas; Bridge as faz ANTES QUE existem...
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class IRemoteControl(ABC):
    """ Remote Control Interface"""

    @abstractmethod
    def increase_volume(self) -> None: pass

    @abstractmethod
    def decrease_volume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass

class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None: 
        self._device.volume -= 10

    def power(self) -> None: 
        self._device.power = not self._device.power

class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    @abstractmethod
    def volume(self, volume: int) -> None: pass 

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    @abstractmethod
    def power(self, power: bool) -> None: pass 

class TV(IDevice):
    def __init__(self) -> None:
        self._volume: int = 0
        self._power: bool = False
        self._name: str = self.__class__.__name__
    
    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self.power:
            print(f'Please! Turn {self._name} ON')
            return

        if volume > 100 or volume <  0:
            return
        
        self._volume = volume
        print(f'Volume is now {self._volume}.')
    @property
    def power(self) -> bool: 
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power 
        
        print(f'The {self._name} is ON') if self._power else print(f'The {self._name} is OFF')


if __name__ == '__main__':
    device = TV()
    control = RemoteControl(device)

    control.increase_volume()
    control.power()
    control.increase_volume()
    control.increase_volume()
    control.increase_volume()
    
    control.decrease_volume()
    control.decrease_volume()
    control.decrease_volume()
    control.power()
    control.decrease_volume()