"""
Façade (Fachada) é um padrão de projeto estrutural que tem a intenção de fornecer uma interface unificada para um conjunto de interfaces em um subsistema. Façade define uma interface de nivel mais alto que torna o subsistema mais fácil de ser usado.
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

class WeatherStationFacade:
    def __init__(self,) -> None:
        self.weather_station = WeatherStation()
        self.weather_station.create_observer('Iphone14', Smartphone)
        self.weather_station.create_observer('Iphone12', Smartphone)

    def create_observer(self, name: str, observer: IObserver) -> IObserver:
        observer = observer(name, self.weather_station)
        self.weather_station.add_observer(observer)
        return observer

    def add_observer(self, observer: IObserver) -> None:
        self.weather_station.add_observer(observer)
    
    def remove_observer(self, observer: IObserver) -> None:
        self.weather_station.remove_observer(observer)  
    
    def change_state(self, state: Dict) -> None:
        self.weather_station.state = state        

    def reset_state(self) -> None:
        self.weather_station.reset_state()

if __name__ == '__main__':
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '30'})
    weather_station.change_state({'temperature': '32'})
    weather_station.change_state({'humidity': '30'})

    
    weather_station.remove_observer()

    weather_station.reset_state()