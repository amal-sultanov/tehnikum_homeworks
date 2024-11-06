class Animal:
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return 'Woof, woof'


class Cat(Animal):
    def make_sound(self):
        return 'Meow, meow'


class Cow(Animal):
    def make_sound(self):
        return 'Moo, moo'


dog = Dog()
print(dog.make_sound())

cat = Cat()
print(cat.make_sound())

cow = Cow()
print(cow.make_sound())


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return f'Brand: {self.brand}, year: {self.year}'


class Car(Vehicle):
    def __init__(self, brand, year, wheels, doors):
        super().__init__(brand, year)
        self.wheels = wheels
        self.doors = doors

    def display_info(self):
        return (f'Brand: {self.brand}, year: {self.year}, '
                f'wheels: {self.wheels}, doors: {self.doors}')


class Motorcycle(Vehicle):
    def __init__(self, brand, year, wheels, helmets):
        super().__init__(brand, year)
        self.wheels = wheels
        self.helmets = helmets

    def display_info(self):
        return (f'Brand: {self.brand}, year: {self.year}, '
                f'wheels: {self.wheels}, helmets: {self.helmets}')


car = Car('Chevrolet', 2000, 4, 4)
print(car.display_info())

motorcycle = Motorcycle('BMW', 2010, 2, 1)
print(motorcycle.display_info())
