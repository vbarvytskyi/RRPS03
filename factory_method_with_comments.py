# Патерн Factory Method (Фабричний метод)
# Патерн створює об'єкти без необхідності вказувати їх точний тип у коді.
# Це корисно для забезпечення гнучкості та розширюваності.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        # Фабрика вирішує, який саме об'єкт створити залежно від параметру
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

# Використання Factory Method
# Ми можемо створити різні об'єкти, не змінюючи логіку їх створення.
animal = AnimalFactory.create_animal("dog")
print(animal.speak())  # Woof!
