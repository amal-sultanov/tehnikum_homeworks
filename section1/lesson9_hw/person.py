class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person('Bob', 20)
person2 = Person('Jack', 43)

print(f'Object 1: name - {person1.name}, age - {person1.age}')
print(f'Object 2: name - {person2.name}, age - {person2.age}')
