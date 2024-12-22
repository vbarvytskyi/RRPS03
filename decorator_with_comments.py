# Патерн Decorator (Декоратор)
# Дозволяє динамічно додати нову функціональність до об'єкта, не змінюючи його структури.
# Це корисно для створення багаторівневих модифікацій об'єктів.

class Coffee:
    def cost(self):
        return 5  # Базова вартість кави

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        # Додаємо вартість молока до базової вартості кави
        return self._coffee.cost() + 2

# Використання Decorator
# Ми можемо додавати додаткову функціональність, наприклад, молоко до кави.
coffee = Coffee()
milk_coffee = MilkDecorator(coffee)
print(milk_coffee.cost())  # 7
