# class Animal:
#     def make_sound(self, s):
#         print(s)
#
#
# class Horse(Animal):
#     pass
#
#
# horse = Horse()
# horse.make_sound('sound')


# class A:
#     def __init__(self, x):
#         self.x = x
# 
#     def print_x(self):
#         return self.x
# 
# 
# class B(A):
#     pass
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(model, color, year)
#         self.sponsor = sponsor

# class Calculator:
#     @classmethod
#     def sum(cls, a, b):
#         return a + b
#
#
# print(Calculator.sum(1, 2))

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     @property
#     def area(self):
#         return self.width * self.height
#
#
# rectangle = Rectangle(10, 20)
# print(rectangle.area)
# rectangle.height = 5
# print(rectangle.area)

# class Worker:
#     def __init__(self, name, age, position):
#         self.name = name
#         self.age = age
#         self.position = position
#
#
# class HR(Worker):
#     def show_position(self, worker):
#         return worker.name, worker.position
#
#
# worker1 = Worker('Bob', 18, 'position')
# print(vars(worker1))
# hr = HR('Jake', 30, 'hr')
# print(hr.show_position(worker1))

class Player:
    def __init__(self, power, velocity, accuracy, stamina):
        self.power = power
        self.velocity = velocity
        self.accuracy = accuracy
        self.stamina = stamina


class Attacker(Player):
    def __init__(self, power, velocity, accuracy, stamina):
        super().__init__(power, velocity, accuracy, stamina)

    def dribble(self):
        return 'I can dribble well and score'


class Defender(Player):
    def __init__(self, power, velocity, accuracy, stamina):
        super().__init__(power, velocity, accuracy, stamina)

    def steal(self):
        return 'I can steal the ball better than others'


class Midfielder(Player):
    def __init__(self, power, velocity, accuracy, stamina):
        super().__init__(power, velocity, accuracy, stamina)

    def link(self):
        return 'I can link the play between attackers and defenders'


class Goalkeeper(Player):
    def __init__(self, power, velocity, accuracy, stamina):
        super().__init__(power, velocity, accuracy, stamina)

    def save(self):
        return 'I can save the ball by using both hands and legs'
