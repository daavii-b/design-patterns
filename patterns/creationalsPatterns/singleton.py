"""
O singleton tem a intenção de garantir que uma classe tenha somente uma instância e fornece um ponto global de acesso para a mesma.

When discussing about which pattern to drop, we found that we still love them all.
(Not really i'm in favor of dropping Singleton. 
It's use is almost always a design smell.)
Erich Gamma, em entrevista para o InformIT
"""



def singleton(clas):
    """
    Singleton como um decorador.
    Usando essa abordagem, evitamos o problema de ter a execução do inicializador repetidas vezes.
    """
    instances = {}
    
    def get_class(*args, **kwargs):
        if clas not in instances:
            instances[clas] = clas(*args, **kwargs)
        return instances[clas]
    return get_class


@singleton
class AppSettings:
    """
    Este tipo de Singleton tem um problema relacionado ao inicializador da classe.
    Toda vez que for instanciada, o inicializador será executado, podendo gerar algum comportamento indesejado.
    """
    _instance = None
    def __new__(cls,  *args, **kwargs) -> object:
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        """
        O init sempre será executado para cada nova instância da classe.
        """
        print('Nova instância criada')
        self.tema = 'Escuro'

"""
Criando um singleton com Meta Class em Python.
"""

class Meta(type):
    def __call__(self, *args, **kwargs):
        print('Sou o primeiro a ser executado.')
        return super().__call__(*args, **kwargs)


class Person(metaclass=Meta):
    """
    Esta classe é apenas um exemplo do funcionamento dos métodos especiais em Python.
    Criamos os métodos new, call, e init.
    Também que criamos uma metaclase para usarmos como exemplo.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, nome: str, *args, **kwargs):
        self.nome = nome

    def __call__(self, qualities: str):
        print(f'Minha qualidades são: {qualities}')


"""
Criando o Singleton
"""
from typing import Dict, Any

class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class SystemSettings(metaclass=Singleton):
    def __init__(self) -> None:
        self.tema: str = 'Claro'
        self.font: float = 18.5


if __name__ == '__main__':
    # Exemplos usando a classe e o decorador.

    as1 = AppSettings()
    as2 = AppSettings()

    
    # Exemplo usando uma metaclass.
    person1 = Person('Daavi')
    person1('Ta em falta')

    # Exemplo usando uma metaclass para criarmos um singleton.

    sys1 = SystemSettings() 
    sys2 = SystemSettings() 

    sys1.tema = 'Escuro'

    print(sys1.tema)
    print(sys2.tema)