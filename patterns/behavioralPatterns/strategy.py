"""
Strategy é um padrão comportamental que tem a intenção de definir uma familia de algoritmos, encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.

Princípio (Open / Closed):
 - Entidades devem ser abertas para extensões,  mas fechadas para modificações.
"""

from abc import ABC, abstractmethod
class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'


    def __repr__(self) -> str:
        return self.__str__()



class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class Order(StringReprMixin):
    def __init__(self, total: float, discount: DiscountStrategy) -> None:
        self._total = total
        self._discount = discount
    @property        
    def total(self):
        return self._total
    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)


class FivePercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return f'{value - (value * 0.05)} - discount: 5%'
class TenPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return f'{value - (value * 0.1)} - discount: 10%'
class TwelvePercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return f'{value - (value * 0.12)} - discount: 12%'
class FifteenPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return f'{value - (value * 0.15)} - discount: 15%'
class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return f'{value - (value * 0.2)} - discount: 20%'

class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return f'{value} - discount: 0%'

class CustomDiscount(DiscountStrategy):
    def __init__(self, discount: float) -> None:
        self._discount = (discount / 100)
    
    def calculate(self, value: float) -> float:
        return f'{value - (value * self._discount)} - discount: {(self._discount * 100):.0f}%'

if __name__ == '__main__':
    discount = TwentyPercent()
    order = Order(1000, discount)

    print(order.total)
    print(order.total_with_discount)
    print("="*50)
    
    discount = FifteenPercent()
    order = Order(45000, discount)
    print(order.total)
    print(order.total_with_discount)
    print("="*50)
    
    discount = FivePercent()
    order = Order(200, discount)

    print(order.total)
    print(order.total_with_discount)
    print("="*50)
    
    discount = TenPercent()
    order = Order(1000, discount)

    print(order.total)
    print(order.total_with_discount)
    print("="*50)

    discount = TwelvePercent()
    order = Order(1000, discount)

    print(order.total)
    print(order.total_with_discount)
    print("="*50)
    
    discount = NoDiscount()
    order = Order(1000, discount)

    print(order.total)
    print(order.total_with_discount)
    print("="*50)
    
    discount = CustomDiscount(50)
    order = Order(1000, discount)

    print(order.total)
    print(order.total_with_discount)
    print("="*50)
