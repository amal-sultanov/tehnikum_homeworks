# p = ['m', 'my', 23]
#
# for i in p:
#     print(i)

# my_list = [6, 4, '2']
#
# for i in my_list:
#     print(i + 2)

# names = ['Ivan', 'Pavel', 'Jordan', 5]
#
# for i in range(1, 20):
#     if 'Pavel' in names:
#         print('Pavel is in the list')
#     else:
#         print('No idea who is it')

# words = ['adopt', 'bake', 'beam', 'confide', 'grill', 'wave']
# past_tense = []
#
# for word in words:
#     if word[-1] != 'e':
#         past_tense.append(word + 'ed')
#     else:
#         past_tense.append(word + 'd')
#
# print(past_tense)

# p = ['m', 'my', 23]
# i = 0
#
# while i < len(p):
#     print(p[i])
#     i += 1 

names = ['Bob', 'David']
telephone_numbers = ['909998877', '997776655']
operations = ['add', 'change', 'remove']
print('Operations with: 1) names, 2) phone numbers')
operation = input('Enter operation: ')

while True:
    if operation == '1':
        print('Operations: 1) add name, 2) change name, 3) remove name')
        choice = input('Enter your choice: ')

        if choice == '1':
            name = input('Enter a name: ')
            names.append(name)
            print(names)
        elif choice == '2':
            name_to_change = input('Enter a name to change: ')
            new_name = input('Enter a new name: ')
            index = names.index(name_to_change)
            names[index] = new_name
            print(names)
        elif choice == '3':
            name_to_remove = input('Enter a name to remove: ')
            names.remove(name_to_remove)
            print(names)
        else:
            print('Wrong operation')

    elif operation == '2':
        print('Operations: 1) add number, 2) change number, 3) remove number')
        choice = input('Enter your choice: ')

        if choice == '1':
            number = input('Enter a number: ')
            telephone_numbers.append(number)
            print(telephone_numbers)
        elif choice == '2':
            number_to_change = input('Enter a number to change: ')
            new_number = input('Enter a new number: ')
            index = telephone_numbers.index(number_to_change)
            telephone_numbers[index] = new_number
            print(telephone_numbers)
        elif choice == '3':
            number_to_remove = input('Enter a number to remove: ')
            telephone_numbers.remove(number_to_remove)
            print(telephone_numbers)
