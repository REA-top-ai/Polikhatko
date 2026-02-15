# # 14.Модули
# # Задание 1
# from datetime import datetime
# current_time = datetime.now()
# print(current_time)
#
# # Задание 2
# 1)
import random
# 2)
random_list = [random.randint(1, 100) for _ in range(101)]
# 4)
randomer_number = random.choice(random_list)
print(randomer_number)

# Задание 3 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# import matplotlib.pyplot as plt
# import random
#
# number_a = range(1, 13)
# number_b = random.sample(range(1000), 12)
#
# plt.plot(number_a, number_b)
# plt.title("Случайные данные")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.grid(True)
# plt.show()


# задание 4

# # задание 5
# import random
# player_numbers = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707, 808, 909, 111, 222, 333]
#
# admin_number = random.randint(1, 9)
#
# print(f"Администрация загадала число: {admin_number}")
#
# winners_count = 0
# max_winners = 5
#
# for number in player_numbers:
#     digit_sum = sum(int(digit) for digit in str(number))
#
#     if digit_sum % admin_number == 0:
#         print(f"Выиграл номер: {number}")
#         winners_count += 1
#
#         if winners_count >= max_winners:
#             print("Розыгрыш окончен.")
#             break
#
# if winners_count < max_winners:
#     print("Розыгрыш окончен.")
# # задание 6
# import random
# attempts = int(input("Введите количество бросков: "))
# outcomes = ["Орел", "Решка"]
# for _ in range(attempts):
#     result = random.choice(outcomes)
#     print(result)
# # задание 7
# import random
# attempts = int(input("Введите количество бросков: "))
# for _ in range(attempts):
#     result = random.randint(1, 6)
#     print(result)
# задание 8
import random
import string

length = int(input("Введите длину пароля: "))

chars = string.ascii_letters

password = ''.join(random.choice(chars) for _ in range(length))

print("Сгенерированный пароль:", password)
