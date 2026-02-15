# 4.Работа со строками
# задание 1
favour_word = "Python"
print(favour_word)

# задание 2
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
print("Имя учетной записи:", new_account)

temp_password = last_name[2:6]
print("Временный пароль:", temp_password)

# задание 3
def password_generator(first_name, last_name):
    last_three_first = first_name[-3:]
    last_three_last = last_name[-3:]
    return last_three_first + last_three_last

first_name = "Алексей"
last_name = "Иванов"
temp_password = password_generator(first_name, last_name)
print(temp_password)

# задание 4
def password_generator(first_name, last_name):
    last_three_first = first_name[-3:]
    last_three_last = last_name[-3:]
    return last_three_first + last_three_last

first_name = "Анна"
last_name = "Петрова"
temp_password = password_generator(first_name, last_name)

print(temp_password)

# задание 5
company_motto = "Мечты сбываются"

second_to_last = company_motto[-2]
print(second_to_last)

final_word = company_motto[-4:]
print(final_word)

# задание 6
first_name = "роб"
fixed_first_name = "Р" + first_name[1:]
print(fixed_first_name)

# задание 7
password = "theycallme\"crazy\"91"
print(password)

# задание 8
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)


