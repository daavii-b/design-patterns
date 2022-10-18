"""
O padrão Observer tem a intenção de definir uma depedência de um-para-muitos entre objetos, de maneira que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

Um observer é um objeto que gostaria de ser informado, um observable (subject) é a entidade que gera as informações.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """Observable Interface"""
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass
    
    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass
    
    @abstractmethod
    def notify_observers(self) -> None: pass

class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class WeatherStation(IObservable):
    """Observable"""
    def __init__(self) -> None:
        self._observers: List[IObserver] = list()
        self._state: Dict = dict()
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()
    
    def add_observer(self, observer: IObserver) -> None: 
        self._observers.append(observer)
    
    def remove_observer(self, observer: IObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class Smartphone(IObserver):
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable
    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou de ser atualizado => {self.observable.state}')
    

if __name__ == '__main__':
    weather_station = WeatherStation()
    smartphone = Smartphone('Iphone14', weather_station)
    smartphone_2 = Smartphone('Iphone12', weather_station)
    weather_station.add_observer(smartphone)
    weather_station.add_observer(smartphone_2)

    weather_station.state = {'temperature': '30'}
    weather_station.state = {'temperature': '32'}
    weather_station.state = {'humidity': '30'}
    
    weather_station.remove_observer(smartphone)
    weather_station.state = {'humidity': '30', 'weather': 'sunny'}
    weather_station.reset_state()