names = [1, 2, 3, 4, ['hello', 3, 5]]

print(len(names))
print(names[0])
print(names[4][0])

numbers = [1, 2, 3, 4, 5]

print(numbers)
print(numbers[1], numbers[3])

colors = ['red', 'yellow', 'green', 'black', 'white']

print(colors[:3])

numbers.append(6)
print(numbers)
numbers.insert(0, 0)
print(numbers)

numbers.extend([7, 8, 9, 10])
print(numbers)

numbers.remove(1)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
numbers.clear()
print(numbers)

names = []
name = input('Enter a name: ')
names.append(name)
print(f'Current list of names: {names}')
