# x = {'name': 'Pasha', 'job': 'TGbot creator'}
# print(x['job'])

# instructor = {'name': 'Jordan', 'age': 21}
# instructor.pop('age')
# print(instructor)
# instructor.clear()
# print(instructor)

# for v in instructor.keys():
#     print(v)
#
# for v in instructor.values():
#     print(v)
#
# for k, v in instructor.items():
#     print(k, v)

# game_properties = ["current_score", "high_score", "number_of_lives",
#                    "items_in_inventory", "power_ups", "ammo",
#                    "enemies_on_screen", "enemy_kills", "enemy_kill_streaks",
#                    "minutes_played", "notifications", "achievements"]
#
# new_player = {}.fromkeys(game_properties, 0)
# print(new_player)

products = {}

while True:
    print("Enter 'add' to add a product or 'products' to see what you have")
    option = input('Enter your option: ')

    if option == 'add':
        product = input('Enter product name: ')
        quantity = int(input('Enter quantity: '))
        products[product] = quantity
    elif option == 'products':
        print(products)
