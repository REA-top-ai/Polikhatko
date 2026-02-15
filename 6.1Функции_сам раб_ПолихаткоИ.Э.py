# задача 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

f100_in_celsius = f_to_c(100)
print(f"100°F = {f100_in_celsius:.2f}°C")

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print(f"0°C = {c0_in_fahrenheit}°F")


# задача 2
def get_force(mass, acceleration):
    return mass * acceleration

train_mass = 1000
train_acceleration = 5
train_distance = 20

train_force = get_force(train_mass, train_acceleration)

print(train_force)

print(f"Поезд посылает {train_force} Н силы")
# задача 3
def print_meal_plan(meal):
    print("мои предпочтения в еде")
    print(f"Завтрак: {meal[0]}")
    print(f"Обед: {meal[1]}")
    print(f"Ужин: {meal[2]}")

daily_meals = ["овсянка", "суп", "котлета с гарниром"]
print_meal_plan(daily_meals)

# задача 4
def check_login(user_name, ARM):
    valid_logins = {
        "Дмитрий": 1,
        "Ангелина": 2,
        "Василий": 3,
        "Екатерина": 4
    }

    if user_name in valid_logins and ARM == valid_logins[user_name]:
        print("Добро пожаловать!")
    elif ARM != valid_logins.get(user_name, -1) and user_name != "Дмитрий":
        print("Логин или пароль не верный, попробуйте еще раз")
    elif ARM != valid_logins.get(user_name, -1) and user_name == "Дмитрий":
        print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

check_login("Дмитрий", 3)
check_login("Ангелина", 2)
check_login("Василий", 5)

# задача 5
def get_grade(grade):
    if grade >= 4.0:
        return "A"
    elif grade >= 3.0:
        return "B"
    elif grade >= 2.0:
        return "C"
    elif grade >= 1.0:
        return "D"
    elif grade >= 0.0:
        return "F"
    else:
        return "Некорректный балл"

print(get_grade(3.7))
print(get_grade(2.5))
print(get_grade(0.9))
print(get_grade(-0.1))