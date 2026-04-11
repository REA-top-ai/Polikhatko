# def add_data(func):
#     def wrapper():
#         return '<data>'+func()+'</data>'
#     return wrapper
#
# def add_name(func):
#     def wrapper():
#         return '<name>'+func()+'</name>'
#     return wrapper
#
#
#
# @add_data
# @add_name
# def add_name():
#     return 'Caclc'
#
# print(add_name())

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Trace calling {func.__name__}()'
              f'with {args}, {kwargs}')
        original = func(*args, **kwargs)
        modified = original.upper()
        print(f'returned {modified}')
        return modified
    return wrapper

@trace
def sey_greet(name, greeting='hello'):
    return f'{name}, {greeting}'

print(sey_greet('Jane'))



