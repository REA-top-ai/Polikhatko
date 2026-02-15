# задание 1
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

# задание 2
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5, last_element)

# задание 3
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase[0:2]
print(beginning)

print(len(beginning))

beginning = suitcase[0:4]
print(beginning)

middle = suitcase[2:4]
print(middle)

# задание 4
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[:3]
print(start)

# задание 5
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

# задание 6
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

# задание 7
# 1
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
# 2
print(games)
print(games_sorted)

# задание 8
inventory = [
    "двухспальная кровать", "двухспальная кровать", "изголовье", "двуспальная кровать",
    "двуспальная кровать", "комод", "комод", "стол", "стол", "тумбочка", "тумбочка",
    "королевский кровать", "двуспальная кровать", "две односпальные кровати",
    "две односпальные кровати", "простыни", "простыни", "подушка", "подушка"
]


# 1
inventory_len = len(inventory)
print(inventory_len)  # Выведет: 19

# 2
first = inventory[0]
print(first)  # Выведет: двухспальная кровать

# 3
last = inventory[-1]
print(last)  # Выведет: подушка

# 4
inventory_2_6 = inventory[2:6]
print(inventory_2_6)

# 5
first_3 = inventory[:3]
print(first_3)

# 6
twin_beds = inventory.count("две односпальные кровати")
print(twin_beds)
# 7
inventory.sort()
print(inventory)


