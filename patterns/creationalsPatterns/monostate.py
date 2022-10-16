"""
Monostate (ou Borg) - É uma variação do Singleton proposto por Alex Martelli que tem a intenção de garantir que o estado do objeto seja igual para a todas as instâncias.
"""


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__()



class Axt(StringReprMixin):
    def __init__(self) -> None:
        self.xtz = 'Tests'
        self.sys = 'Other Tests'    
        

class MonoStateSimple(StringReprMixin):
    _state: dict = {
        'x': 10,
        'y': 20,
    }

    def __init__(self) -> None:
        self.__dict__ = self._state


if __name__ == '__main__':
    m1 = MonoStateSimple()

    print(m1)