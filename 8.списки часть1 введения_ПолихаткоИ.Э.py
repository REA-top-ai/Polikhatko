# задание 1
item = ['торт', 1]
print(item)

# задание 2
household_chemicals = [['стиральный порошок', 1], ['средство для мытья посуды', 1]]
print(household_chemicals)

# задание 3
Names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']

names_and_dogs_names = zip(Names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

# задание 4
orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
print(orders)
orders.append('розы')
print(orders)


# задание 5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

# задание 6
list1 = [1, 8]
list1 = range(9)
print(list(list1))
list2 = range(8)
print(list(list2))


# задание 7
# 1
list1 = range(5, 15, 3)
print(list(list1))
# 2
list2 = range(0, 40, 5)
print(list(list2)) 


