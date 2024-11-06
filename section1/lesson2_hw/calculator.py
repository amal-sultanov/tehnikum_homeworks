first_number = int(input('Enter the first number: '))
operation = input('Enter the operation (+, - ,*, /): ')
second_number = int(input('Enter the second number: '))

if operation == '+':
    print(f'Result: {first_number + second_number}')
elif operation == '-':
    print(f'Result: {first_number - second_number}')
elif operation == '*':
    print(f'Result: {first_number * second_number}')
elif operation == '/':
    print(f'Result: {first_number / second_number}')
else:
    print('Invalid operation, enter one from listed')
