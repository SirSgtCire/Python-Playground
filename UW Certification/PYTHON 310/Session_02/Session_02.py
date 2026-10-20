# Formatting
sentence='Hello, my name is Edig, and I am a student in this course.\nMy favorite color happens to be chroma.'
print(sentence)

sentence2='Byeah we workin with escape \"characters!\"'
print(sentence2)

sentence3='We are ants on a farm!'
print(sentence3.upper())

sentence4='hello world'
print(sentence4.split(' '))

# YO dot format, we meet again breh!

name=input("Enter your first name: ")
fav_color=input("Enter your favorite color: ")
fav_number=int(input("Enter your favorite number: "))
print('Hello {}! Your favorite color is {} and number is {}!'.format(name, fav_color, fav_number))

template_string0='Hello {}! Your favorite color is {} and number is {}!'
template_string1='Hello {0}! Your favorite color is {1} and number is {2}!'
template_string2='Hello {name}! Your favorite color is {color} and number is {number}!'
print(template_string0.format(name, fav_color, fav_number))
print(template_string1.format(name, fav_color, fav_number))
print(template_string2.format(fav_color, fav_number, name))


# Conditionals
clean_my_room = True
wash_the_dishes = True
before_6pm = True

# If I clean my room ,I can watch TV
print(clean_my_room)
if clean_my_room:
    print('You can watch TV')

# If I clean my room AND wash the dishes, I can play video games
print(clean_my_room and wash_the_dishes)
if clean_my_room and wash_the_dishes:
    print('You can play video games')

# IF I clean my room OR wash the dishes, I can watch TV
print(clean_my_room or wash_the_dishes)
if clean_my_room or wash_the_dishes:
    print('You can watch TV')

# If I do NOT clean my room and do NOT wash the dishes, I must go to bed
print((not clean_my_room) and (not wash_the_dishes))
if (not clean_my_room) and (not wash_the_dishes):
    print('Bedtime!')

assert True == True
assert clean_my_room or wash_the_dishes
assert 2+2 == 4
assert 2+2 != 5

if clean_my_room and wash_the_dishes:
    print('You can play video games')
elif clean_my_room or wash_the_dishes:
    print('You can watch TV')
else:
    print('You can go to bed')

# Functions
def print_hello():
    print('Hello world!')

def get_user_name():
    first_name = input('What is your first name? ')
    return first_name

def greet_user(by_first_name):
    print(f'Hello, {by_first_name.capitalize()}!')

if __name__ == '__main__':
    print_hello()
    greet_user(get_user_name())

# Exceptions


# Conditionals