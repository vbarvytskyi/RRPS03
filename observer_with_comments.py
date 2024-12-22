# Патерн Observer (Спостерігач)
# Дозволяє одному об'єкту (Subject) сповіщати інші об'єкти (Observers) про зміну свого стану.
# Це корисно для реалізації системи підписок і сповіщень.

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Отримано повідомлення: {message}")

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        # Додаємо спостерігача до списку
        self._observers.append(observer)

    def notify_observers(self, message):
        # Сповіщаємо всіх спостерігачів про зміну
        for observer in self._observers:
            observer.update(message)

# Використання Observer
# Один об'єкт може сповіщати кількох про зміну свого стану.
subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify_observers("Привіт, Спостерігачу!")
