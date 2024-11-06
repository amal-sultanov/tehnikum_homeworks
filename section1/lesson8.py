# x = lambda e: e
# print(x(9))

# a = lambda x: 4 * x
# print(a(2))

# def spam(a, b, c=9):
#     print(a + b + c)
#
#
# spam(1, 2)

# def addition(number1, number2):
#     return number1 + number2
#
#
# print(addition(2, 3))


# def spammer(*args):
#     for i in args:
#         print(i)
#
#
# spammer(1, 2, 3, 4, 5)


# def spam(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#
#
# spam(name='Bob', age=21)

clients = {}
available_rooms = [i for i in range(1, 21)]
booked_rooms = []


def add_client(name, room):
    clients[name] = room
    available_rooms.remove(room)
    # booked_rooms.append(room)
    booked_rooms.insert(room - 1, room)


def delete_client(name):
    booked_rooms.remove(clients[name])
    # available_rooms.append(clients[name])
    available_rooms.insert(clients[name] - 1, clients[name])
    clients.pop(name)


def show_booked_rooms():
    return booked_rooms


while True:
    print('1) add a client, 2) delete a client, 3) show booked rooms')
    option = input('Enter your option: ')

    if option == '1':
        client_name = input('Enter a client name: ')
        print(available_rooms)
        client_room = input('Enter a room number: ')

        if client_room in available_rooms:
            add_client(client_name, client_room)
        else:
            print('Room is already booked or incorrect input')

        print('Added successfully')

    elif option == '2':
        client_name = input('Enter a client name to delete: ')

        if client_name in clients:
            delete_client(client_name)
            print('Deleted successfully')
        else:
            print('Client does not exist')
    elif option == '3':
        print(show_booked_rooms())
    else:
        print('Invalid input')
