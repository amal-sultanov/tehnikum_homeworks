# lesson 2 (variables, data types, mathematical operators,
# string formatting, conditional operators)
text = 'some text'
number = 5
answer = 2 + 3 + 8 * 8
result = 'Result of previous expression is {}'.format(answer)

if text == 'some text':
    print(True)
elif text == 'some other text':
    print(False)
else:
    print(None)

# lesson 3 (lists, indexing, tuples)
numbers = [3, 5, 6, 4, 3, 2]
numbers[0] = 7
sliced_numbers = numbers[1::3]
numbers.append(9)
numbers.clear()

names = ('Bob', 'David', 'Jack', 'Alice')
print(names[-1])
new_tuple = tuple([4235, 576, 2452, 134, 67568])
is_inside = 'Bob' in names

# lesson 4 (loops, range())
for i in range(5):
    print(i)

counter = 1
while counter != 0:
    print(counter)
    counter -= 1

# lesson 5 (list comprehensions)
characters = [char for char in 'VERY LONG STREAM OF CHARACTERS']
even_numbers = [i for i in range(11) if i % 2 == 0]

# lesson 6 (dictionaries, sets)
clients = {1: 'Bobby', 2: 'David', 3: 'Ronnie'}
clients[4] = 'Dan'
print(clients.values())
clients.pop(1)

for key, value in clients.items():
    print(key, value)

elements = set([1, 1, 2, 4, 5, 5, 3, 7, 8, 7, 8])
unique_elements = {1, 2, 4, 5, 7, 8}

# lesson 7 (functions, third party libraries installation, parsing)
import requests


def greet(name):
    return f'Hello, {name}!'


link = 'https://icanhazip.com/'
print(requests.get(link).text)

# lesson 8 (lambda functions, parameters and arguments, *args, **kwargs)
sum_numbers = lambda x, y: x + y


def add(x, y):
    return x + y


def show_parameters(a, b, *args, **kwargs):
    return a, b, args, kwargs


print(add(1, 2))
print(show_parameters(1, 2, 5, 7, 8, 3, name='Tom', age=50))


# lesson 9 (OOP, classes, __init__, objects, methods vs functions)
def simple_function():
    pass


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_details(self):
        return self.name, self.id


user = User(1, 'John')
print(user.show_details())


# lesson 10 (inheritance, super(), multiple inheritance,
# @classmethod, @property)
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def class_info(cls):
        return cls.__name__


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    @property
    def show_details(self):
        return self.a, self.b, self.c


class C:
    pass


class D(A, C):
    pass


b = B(1, 2, 3)
print(A.class_info())
print(b.show_details)

# lesson 11 (git, GitHub)
# git config --list: посмотреть все настройки системы
# git --help: выводит общую документацию по git
# git log --help: предоставит нам документацию по какой-то определенной команде (в данном случае это - log)
# git init: создает репозиторий в текущей директории
# git status: показывает информацию о текущем состоянии репозитория
# git add file: добавляет изменения в коммит
# git reset file: удаляет подготовленный для коммита файл
# git commit -m '': создает сам коммит с названием
# git log: покажет историю коммитов
# git show hash_commit: покажет операции в списке изменений
# git clone: копирует удаленный репозиторий
# git remote add origin: связывает локальный репозиторий с репозиторием на GitHub (главный репозиторий называется origin)
# git push origin master: пересылает локальный коммит на сервер (master — это ветка по умолчанию для всех репозиториев)
# git pull origin master: скачает изменения с удаленного репозитория
# rm -r .git: удаляет локальный репозиторий
# git branch: создает новую ветку
# git checkout: переключает на другую ветку
# git merge: объединяет ветки
# git branch -d: удаляет ветку
# .gitignore: игнорирует файлы, перечисленные тут при добавлении в коммит
