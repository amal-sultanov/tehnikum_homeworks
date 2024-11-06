# numbers = [i for i in range(100)]
# print(numbers)

# my_list = [1, 'a', 2, 4.5]
# my = [i + 2 for i in my_list]
#
# print(my)

# names = ['Pavel', 'Sasha', 'Jordan', 'Pasha']
# answer = [i[0] for i in names]
#
# print(answer)

# nums1 = [i for i in range(1, 21)]
# nums2 = [i for i in range(1, 21) if i % 2 == 0]
#
# print(nums1)
# print(nums2)

usernames = []

while True:
    new_name = input('Enter a new name: ')

    if new_name in usernames:
        print(f'{new_name} is already in list, try another one')
    else:
        usernames.append(new_name)
        print(f'{new_name} was successfully added')

    print(usernames)
