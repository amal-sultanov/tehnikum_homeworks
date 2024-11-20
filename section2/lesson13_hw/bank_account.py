import sqlite3

connection = sqlite3.connect('bank_accounts.db')
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS bank_accounts "
            "(id INTEGER PRIMARY KEY, surname TEXT, name TEXT, "
            "patronymic TEXT, phone_number TEXT, balance REAL);")


def register_client(surname, name, patronymic, phone_number):
    sql.execute(f"INSERT INTO bank_accounts "
                "(surname, name, patronymic, phone_number, balance) "
                "VALUES (?, ?, ?, ?, ?);",
                (surname, name, patronymic, phone_number, 0))
    connection.commit()


def search_by_fullname(surname, name, patronymic):
    result = sql.execute(f"SELECT * FROM bank_accounts "
                         f"WHERE surname='{surname}' AND name='{name}' "
                         f"AND patronymic='{patronymic}';")
    return result.fetchone()


def search_by_phone_number(phone_number):
    result = sql.execute(f"SELECT * FROM bank_accounts "
                         f"WHERE phone_number={phone_number};")
    return result.fetchone()


def refill_balance(id, amount):
    sql.execute(f"UPDATE bank_accounts SET balance=balance+{amount} "
                f"WHERE id={id};")
    connection.commit()


def withdraw(id, amount):
    sql.execute(f"UPDATE bank_accounts SET balance=balance-{amount} "
                f"WHERE id={id};")
    connection.commit()


def show_balance(id):
    result = sql.execute(f"SELECT balance FROM bank_accounts WHERE id={id};")
    return result.fetchone()


def calculate_investment(amount, month_count):
    profit = amount * 0.01 * month_count / 365 * 30 / 100
    return '%.2f' % profit


def show_profile(id):
    result = sql.execute(f"SELECT * FROM bank_accounts WHERE id={id};")
    return result.fetchone()


def show_all_clients():
    result = sql.execute("SELECT * FROM bank_accounts;")
    return result.fetchall()


while True:
    print(f'Our clients:\n{show_all_clients()}\n')
    print('Available operations:')
    print('0) add new client\n1) search by fullname\n'
          '2) search by phone number\n3) refill balance\n4) withdraw money\n'
          '5) show balance\n6) calculate investment\n7) show profile\n8) exit')
    option = input('Enter your option: ')

    if option == '0':
        new_surname = input('Enter new surname: ')
        new_name = input('Enter new name: ')
        new_patronymic = input('Enter new patronymic: ')
        new_phone_number = input('Enter new phone number: ')
        register_client(new_surname, new_name,
                        new_patronymic, new_phone_number)
        print('New client has been registered')
    elif option == '1':
        surname, name, patronymic = input(
            'Enter full name to search (Surname Name Patronymic): '
        ).split(' ')
        print(f'Result: {search_by_fullname(surname, name, patronymic)}')
    elif option == '2':
        phone_number = input('Enter phone number to search: ')
        print(f'Result: {search_by_phone_number(phone_number)}')
    elif option == '3':
        id = int(input('Enter id of client: '))
        amount = float(input('How much money would you like to refill?: '))
        refill_balance(id, amount)
        print('You have successfully refilled the balance')
    elif option == '4':
        id = int(input('Enter id of client: '))
        amount = float(input('How much money would you like to withdraw?: $'))
        withdraw(id, amount)
        print('You have successfully withdrawn the money')
    elif option == '5':
        id = int(input('Enter id of client: '))
        print(f'Result: {show_balance(id)}')
    elif option == '6':
        amount = float(input('How much money would you like to deposit?: $'))
        month_count = int(input('For how many months? (12, 24, 36): '))
        print(f'Under these conditions you may '
              f'get +${calculate_investment(amount, month_count)}')
    elif option == '7':
        id = int(input('Enter id of client: '))
        print(f'Result: {show_profile(id)}')
    elif option == '8':
        connection.close()
        break
    else:
        print('Wrong option')
