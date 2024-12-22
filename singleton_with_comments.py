# Патерн Singleton (Одинак)
# Патерн забезпечує, що клас має лише один екземпляр. 
# Це корисно, наприклад, для керування глобальними ресурсами або конфігурацією програми.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Використання Singleton
# При створенні кількох об'єктів класу Singleton всі вони будуть посилатися на один і той самий екземпляр.
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True, оскільки об'єкти є одним і тим самим екземпляром
