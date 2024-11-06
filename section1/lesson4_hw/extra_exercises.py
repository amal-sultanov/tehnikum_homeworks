# 5
print('small bottles: volume is less then or equal to 1 l, $0.10 per bottle\n'
      'large bottles: volume is bigger than 1 l, $0.25 per bottle')
small_bottles = int(input('Enter the number of small bottles: '))
large_bottles = int(input('Enter the number of large bottles: '))
result = small_bottles * 0.10 + large_bottles * 0.25
print('Amount of money you can receive $%.2f' % result)

# 6
# bill = float(input('Enter your bill: $'))
# tax = bill * 12 / 100
# tip = bill * 18 / 100
# total = bill + tax + tip
#
# print('Tax: $%.2f, tip: $%.2f, total: $%.2f' % (tax, tip, total))

# 7
# number = int(input('Enter a number: '))
# result = (number * (number + 1)) / 2
# print(f'Sum of first {number} positive natural numbers: {result}')

# 8
# print('Souvenirs weigh 75 g, toys 112 g')
# souvenirs = int(input('Enter the number of souvenirs you want to buy: '))
# trinkets = int(input('Enter the number of trinkets you want to buy: '))
# print(f'Net weight: {souvenirs * 75 + trinkets * 112} g')
