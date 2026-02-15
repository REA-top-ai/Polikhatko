# 11.Цыклы
# Задание 1
# 1)
# board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
# sport_games = ['football', 'football- American', 'hockey ', 'baseball', 'cricket']
#
# for game in board_games:
# print(game) #код с ошибко
# 2)
# board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
# sport_games = ['football', 'football- American', 'hockey ', 'baseball', 'cricket']
# for game in board_games:
#     print(game) #правильный код
# # 3)
# for sport in sport_games:
#     print(sport)

# Залание 2
# a = "I will not chew gum in class"
# for i in range(5):
#     print(a)

# Задание 3
# 1)
# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
# # 2) и 3)
# for student in students_period_A:
#     students_period_B.append(student)
#     print(student)

# Задание 4
# dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
# dog_breed_I_want = 'dalmatian'
# for breed in dog_breeds_available_for_adoption:
#     if breed == dog_breed_I_want:
#         print("У них есть собака, которую я хочу!")
#         break
#     print(breed)

# Задание 5
# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
# scoops_sold = 0
# for loc in sales_data:
#     for f in loc:
#         scoops_sold += f
# print(scoops_sold)  #96

# Заданние 6
# 1)
single_digits = list(range(10))
# 3)
squares = []
# 2)
for digit in single_digits:
    print(digit)
# 4)
    squares.append(digit ** 2)
# 5)
print(squares)
# 6)
cubes = [digit ** 3 for digit in single_digits]
# 7)
print(cubes)