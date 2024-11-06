# import requests
#
# url = 'https://api.openweathermap.org/data/2.5/weather'
# params = {'q': 'London',
#           'appid': '159d1093e5a6fab015cd45bcd9b397db',
#           'units': 'metric',
#           'lang': 'ru'}
#
# city = input('Enter city name: ')
# params['q'] = city
# response = requests.get(url, params=params).json()
# print(f'City: {city}\nWeather: {response['weather'][0]['description']}\n'
#       f'Temperature: +{response['main']['temp']}C, '
#       f'feels like +{response['main']['feels_like']}C')


# class User:
#     name = 'Jordan'
#
#
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def stop(self):
#         print('Car has been stopped')
#
#     def change_color(self, color):
#         self.color = color
#
#
# car = Car('Gentra', 'white', '2020')
# car.stop()
# car.change_color('black')
# print(car.color)
#
#
# class Comment:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes


# class BankAccount:
#     def __init__(self, client_name, balance=0):
#         self.client_name = client_name
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def cash(self, amount):
#         self.balance -= amount
#
#     def my_balance(self):
#         return self.balance
#
#
# user1 = BankAccount('Bob')
# print(user1.my_balance())
# user1.deposit(10)
# print(user1.my_balance())
# user1.cash(5)
# print(user1.my_balance())


class User:
    def __init__(self, user_name, email, age, phone_number):
        self.user_name = user_name
        self.email = email
        self.age = age
        self.phone_number = phone_number

    def change_username(self, user_name):
        self.user_name = user_name

    def change_phone_number(self, phone_number):
        self.phone_number = phone_number

    def change_email(self, email):
        self.email = email


user = User('David', 'dwefw@fqw.fr', 31, '312354')
print(user.user_name, user.email, user.age, user.phone_number)
user.change_username('Bob')
user.change_phone_number('1234567890')
user.change_email('qwert@eqw.e')
print(user.user_name, user.email, user.age, user.phone_number)
