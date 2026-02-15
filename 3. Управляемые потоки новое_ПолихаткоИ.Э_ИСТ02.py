# 3.Управляемые потоки новое
# Задание 1
# print((6*6)-1 == 8 + 1)
# print(13 - 7 != (3*2) + 1)
# print(3*(2-1)==4-1)

# Задание 2
# print((6*6)-1 >= 8 + 1)
# print(13 - 7 <= (3*2) + 1)
# print(3*(2-1) > 4-1)

# Задание 3
# 1. Ошибка
# bool_variable = true  # NameError: name 'true' is not defined

# 2. Строка
# bool_variable = 'true'
# print(bool_variable)
# print(type(bool_variable))
#
# bool_variable_2 = True
# print(bool_variable_2)
# print(type(bool_variable_2))

# Задание 4
# 1
user_name = "Дмитрий"
# 2
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
# 3
welcome_message = "Добро пожаловать"
# 4
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome_message)
# 5.
print("--- Пример для Дмитрия ---")
user_name = "Дмитрий"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome_message)

print("--- Пример для Ангелины ---")
user_name = "Ангелина"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(welcome_message)



# Задание 5
# 1
enter_number = 2
# 2
if enter_number < 3:
    attempts_left = 3 - enter_number
    print(f"Попробуйте еще раз. У вас осталось {attempts_left} попыток.")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

# 3
print("--- Пример 1: 1 попытка ---")
enter_number = 1
if enter_number < 3:
    attempts_left = 3 - enter_number
    print(f"Попробуйте еще раз. У вас осталось {attempts_left} попыток.")
else:
    print("Вы превысили максимальное число попыток...")

print("--- Пример 2: 3 попытки ---")
enter_number = 3
if enter_number < 3:
    attempts_left = 3 - enter_number
    print(f"Попробуйте еще раз. У вас осталось {attempts_left} попыток.")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

print("--- Пример 3: 5 попыток ---")
enter_number = 5
if enter_number < 3:
    attempts_left = 3 - enter_number
    print(f"Попробуйте еще раз. У вас осталось {attempts_left} попыток.")
else:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

# Задание 6
# Вводим переменные
user_name = input("Введите имя пользователя: ")
ARM = int(input("Введите номер АРМ: "))

# Правильные соответствия
valid_logins = {
    "Дмитрий": 1,
    "Ангелина": 2,
    "Василий": 3,
    "Екатерина": 4
}

# Проверяем соответствие
if user_name in valid_logins and ARM == valid_logins[user_name]:
    print("Добро пожаловать!")
elif ARM != valid_logins.get(user_name, -1) and user_name != "Дмитрий":
    print("Логин или пароль не верный, попробуйте еще раз")
elif ARM != valid_logins.get(user_name, -1) and user_name == "Дмитрий":
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")
# Задание 7
grade = float(input("Введите средний балл (0.0 - 4.0): "))
if grade >= 4.0:
    letter_grade = "A"
elif grade >= 3.0:
    letter_grade = "B"
elif grade >= 2.0:
    letter_grade = "C"
elif grade >= 1.0:
    letter_grade = "D"
elif grade >= 0.0:
    letter_grade = "F"
else:
    letter_grade = "Некорректный балл"
print("Грейд:", letter_grade)