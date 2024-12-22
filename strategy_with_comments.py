# Патерн Strategy (Стратегія)
# Дозволяє визначити набір алгоритмів, інкапсулювати їх і зробити взаємозамінними.
# Це корисно для вибору поведінки під час виконання програми.

class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Сплачено {amount} за допомогою кредитної картки.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Сплачено {amount} за допомогою PayPal.")

class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        # Виконуємо обрану стратегію оплати
        self._strategy.pay(amount)

# Використання Strategy
# Ми можемо динамічно змінювати способи оплати.
payment = PaymentContext(CreditCardPayment())
payment.execute_payment(100)
