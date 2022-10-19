"""
Command tem intenção de encapsular, desta forma permitindo parametrizar clientes com diferentes solicitações, efileirar ou fazer registro(log) de solicitações e suportar operações que podem ser desfeitas

É formado por um cliente, (quem orquestra tudo),  um invoker (que invoca as solicitações), um ou vários objetos de comando (que fazem a ligação entre o receiver a ação a ser executada) e um receiver (o objeto que vai executar a ação no final).
"""  

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    """ Receiver """
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self):
        print(f'{self.name} in {self.room_name} is now ON')
    def off(self) -> None:
        print(f'{self.name} in {self.room_name} is now OFF')

    def change_color(self, color: str):
        self.color = color
        print(f'{self.name} in {self.room_name} is now {self.color}')


class ICommand(ABC):
    """ Command Interface """
    @abstractmethod
    def execute(self) -> None: pass

    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ Concrete Command """
    def __init__(self, light: Light) -> None:
        self.light = light
    
    def execute(self) -> None:
        self.light.on()
    def undo(self) -> None:
        self.light.off()

class LightChangeColor(ICommand):
    """ Concrete Command"""

    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color
    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)
    
    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """ Invoker """
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []
        
        
    def add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def execute_command(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.insert(0, (name, 'execute'))

    def undo_command(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.insert(0, (name, 'undo'))

    def undo_global(self) -> None:
        if not self._undos:
            return None
        for button_name, action in self._undos:

            if action == 'execute':
                self._buttons[button_name].undo()
            else:
                self._buttons[button_name].execute()
            self._undos.pop()

if __name__ == '__main__':
    bedroom_light = Light('Bedroom Light', 'Bedroom')
    bathroom_light = Light('Bathroom Light', 'Bathroom')

    light_on_bedroom = LightOnCommand(bedroom_light)
    light_on_bathroom = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bathroom_light_red = LightChangeColor(bathroom_light, 'Red')

    remote = RemoteController()
    
    
    remote.add_command('Light On Bedroom', light_on_bedroom)
    remote.add_command('Light On Bathroom', light_on_bathroom)
    remote.add_command('Change the light color in Bedroom', bedroom_light_blue)
    remote.add_command('Change the light color in Bathroom', bathroom_light_red)
    
    print('Execute commands')
    remote.execute_command('Light On Bedroom')
    remote.execute_command('Light On Bathroom')
    remote.execute_command('Change the light color in Bedroom')
    remote.execute_command('Change the light color in Bathroom')
    print('='*50)
    remote.undo_command('Light On Bedroom')
    remote.undo_command('Light On Bathroom')
    remote.undo_command('Change the light color in Bedroom')
    remote.undo_command('Change the light color in Bathroom')
    print('='*50)
    
    print('Bellow the undo global is executing')
    remote.undo_global()