"""
O padrão de projeto State é um padrão comportamental que tem a intenção de permitir a um objeto mudar seu comportamento quando seu estado interno muda.


O objeto parecerá ter mudado sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """ Context"""
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()
        
    def approve(self) -> None:
        self.state.approve()
        
    def reject(self) -> None:
        self.state.reject()

class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order
    
    @abstractmethod
    def pending(self) -> None: pass 
    
    @abstractmethod
    def approve(self) -> None: pass 
    
    @abstractmethod
    def rejected(self) -> None: pass 
    
class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order
    
    @abstractmethod
    def pending(self) -> None: pass
    
    @abstractmethod
    def approve(self) -> None: pass
    
    @abstractmethod
    def reject(self) -> None: pass
    
class PaymentPending(OrderState):
    
    def pending(self) -> None:
        print('Pagamento já está pendente.')
 
    
    def approve(self) -> None: 
        self.order.state = PaymentApprove(self.order) 
        print('Pagamento foi aprovado.')

    
    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento foi rejeitado')
 
    
class PaymentApprove(OrderState):
    
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order) 
        print('Pagamento está pendente.')
 
    
    def approve(self) -> None: 
        print('Pagamento já foi aprovado.')

    
    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento foi rejeitado')
    
class PaymentReject(OrderState):
    
    def pending(self) -> None:
        print('Pagamento já foi rejeitado')
 
    
    def approve(self) -> None: 
        print('Pagamento já foi rejeitado')

    
    def reject(self) -> None:
        print('Pagamento já foi rejeitado')


if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.approve()
    order.pending()
    order.reject()
    order.approve()
    order.pending()
