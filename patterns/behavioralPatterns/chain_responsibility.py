"""
Chain of Responsibility (COR) é um padrão comportamental que tem a intenção de evitar o acoplamento de umsa solicitação ao seu receptor, ao dar a mais de um objeto a oportunidade de tratar a solicitação. 
Encadear objetos receptores passando a solicitação ao longo da cadeia até que um objeto a trate.
"""

# Implementando com funções

def handler_ABC(letter: str) -> str:
    letters: list = ['A', 'B', 'C']
    if letter in letters:
        return f'Handler ABC: conseguiu tratar o valor {letter}'
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    letters: list = ['D', 'E', 'F']
    if letter in letters:
        return f'Handler_DEF: conseguiu tratar o valor {letter}'
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
        return f'Handler_unsolved: Não conseguiu tratar sua requisição.'

if __name__ == '__main__':
    print(handler_ABC('A'))
    print(handler_ABC('B'))
    print(handler_ABC('D'))
    print(handler_ABC('G'))
    