# Задание 1
def define_age(current_year, birth_year):
    age = current_year - birth_year
    return age

my_age = define_age(2026, 1990)
print(my_age)

# Задание 2
def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit
low_limit, high_limit = get_boundaries(100, 20)

print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")

# задание 3
def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

lyrics = repeat_stuff("Row", 3) + " Your Boat."
print(lyrics)