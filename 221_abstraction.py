# 221. Abstraction in Object-Oriented Programming (OOP)

# ABC = Abstract Base Class
from abc import ABC, abstractmethod  

class Payment(ABC):  # Abstract class: defines interface for payments
    @abstractmethod
    def process_payment(self) -> None:
        pass  # Abstract method

class CreditCardPayment(Payment): 
    # Implementation of abstract method
    def process_payment(self) -> None:
        print("Processing credit card payment")  

class StripePayment(Payment): 
    # Implementation of abstract method
    def process_payment(self) -> None:
        print("Processing Stripe payment")  

class PayPalPayment(Payment):  
    def process_payment(self) -> None:
        print("Processing PayPal payment")  

# Polymorphism:  same interface, different behaviors
def pay(order_total: float, processor: Payment) -> None:
    print(f"Amount: {order_total}")
    processor.process_payment()  # Calls appropriate method

if __name__ == "__main__":
    pay(1499.0, CreditCardPayment())
    pay(4799.0, StripePayment())
    pay(2299.0, PayPalPayment())
