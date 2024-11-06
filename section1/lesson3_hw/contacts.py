phone_numbers = ['909998877', '998887766']
numbers_list = 'Current list of phone numbers: {}'
print(numbers_list.format(phone_numbers))
print('Operations: 1) add contact, 2) change contact, 3) delete contact')
operation = input('Enter your choice (only number): ')

if operation == '1':
    new_number = input('Enter a new phone number: ')
    phone_numbers.append(new_number)
    print(numbers_list.format(phone_numbers))
elif operation == '2':
    index = int(input('Enter the index (from 0) of the phone number to change: '))
    new_number = input('Enter a new phone number: ')
    phone_numbers[index] = new_number
    print(numbers_list.format(phone_numbers))
elif operation == '3':
    index = int(
        input('Enter the index (from 0) of the phone number to delete: '))
    phone_numbers.pop(index)
    print(numbers_list.format(phone_numbers))
else:
    print('Invalid operation, choose from available ones (only number)')
