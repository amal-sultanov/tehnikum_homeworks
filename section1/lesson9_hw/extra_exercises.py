# 2
# class Student:
#     def __init__(self, name='Ivan', groupNumber='10A', age=18):
#         self.name = name
#         self.groupNumber = groupNumber
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#     def getGroupNumber(self):
#         return self.groupNumber
#
#     def setNameAge(self, new_name, new_age):
#         self.name = new_name
#         self.age = new_age
#
#     def setGroupNumber(self, newGroupNumber):
#         self.groupNumber = newGroupNumber
#
#
# student1 = Student('David', '2B', 8)
# student2 = Student('Bob', '1A', 7)
# student3 = Student('Kate', '11C', 18)
# student4 = Student('John', '8D', 14)
# student5 = Student('Aziz', '5E', 11)

# 3
# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         return self.a + self.b
#
#     def multiplication(self):
#         return self.a * self.b
#
#     def division(self):
#         return self.a / self.b
#
#     def subtraction(self):
#         return self.a - self.b

# 4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return 'Car was started'

    def stop(self):
        return 'Car was stopped'

    def set_year(self, new_year):
        self.year = new_year

    def set_type(self, new_type):
        self.type = new_type

    def set_color(self, new_color):
        self.color = new_color
