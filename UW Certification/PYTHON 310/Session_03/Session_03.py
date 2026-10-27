# Sequences
greeting = 'Hello, my name is Erig! I live in the state of Washington.'
print(greeting)

greeting_length = len(greeting)
print(f'The number of characters in my greeting is: {greeting_length}')
print(f'The first letter in my greeting is: {greeting[0]}')
assert greeting[0] == greeting[-58]
print(f'The last letter in my greeting is: {greeting[57]}')
assert greeting[57] == greeting[-1]
assert greeting[greeting_length-1] == greeting[57]

# [0,5) -> [ is inclusive, ( is exclusive
print(f'The first word in my greeting is: {greeting[0:5]}')
print(f'The first word in my greeting is: {greeting[0:greeting.find(",")]}')
# longhand vs shorthand
print(f'Every other letter is: {greeting[0 : greeting_length : 2]}')
print(f'Every other letter is: {greeting[::2]}')
print(f'String reversed is: {greeting[::-1]}')

# Tuples
my_tuple = (123, "abc", True)
print(my_tuple)
print(type(my_tuple))
# Where is variable in memory
print(id(my_tuple))
temp_tuple = my_tuple
my_tuple += ('hello',)
print(f'temp_tuple = {temp_tuple}')
print(f'my_tuple = {my_tuple}')
print(f'id(temp_tuple) = {id(temp_tuple)}')
print(f'id(my_tuple) = {id(my_tuple)}')

# Lists
my_list = [123, "abc", True]
print(my_list)
print()

temp_list = my_list
my_list += ["hello"]
#VS
my_list.append(3.14)

print(f'temp_list = {temp_list}')
print(f'id(temp_list) = {id(temp_list)}')
print(f'my_list = {my_list}')
print(f'id(my_list) = {id(my_list)}')

print(my_list[0])
print(my_list[-1])
print(my_list[1: len(my_list) - 1])

if 3.14 in my_list:
    print('Mmmmmm, pie :)')
if 'String' in 'This is a String.':
    print('Yay!')
if 'String' not in 'This is a string.':
    print('Sad')

alphabet = ['c', 'b', 'a']
alphacap = sorted(alphabet)
print(alphabet)
print(alphacap)

# Cannot execute sort function within equality check?
alphabet.sort()
if alphacap == alphabet:
    print('Sorta works.')


# Loops
# counter loop
counter = 0
while counter <= 100:
    if counter % 3 == 0 and counter % 5 == 0:
        print('FizzBuzz')
    elif counter % 3 == 0:
        print('Fizz')
    elif counter % 5 == 0:
        print('Buzz')
    else:
        print(counter)
    counter += 1
print('Done!')

# user input loop
user_input = 'n'
age = 10
while user_input == 'n':
    age += 1
    user_input = input(f'Are you {age} years old? ').lower().strip()[0]
print(f'You are {age} years old!')

# while loop
there_yet = 'n'
while there_yet != 'y':
    there_yet = input("Are we there yet?! ").lower().strip()[0]
    user_input = there_yet.lower().strip()[0]
    if len(user_input) <= 0 or user_input[0] != 'y' and user_input != 'n':
        print('Entered diddly squat!')
        break
    if there_yet == 'y':
        print('Gnarf!')
        continue
    if there_yet == 'n':
        print('Doh!')

# for loop
greetings = 'Hello, my name is Erig! I live in the state of Washington.'


# mailroom example
user_input = ''
while user_input != '3':
    user_input = input('1) Send a thank you\n2) Create a report\n3) Quit')
    if not user_input.isdigit() or 1 < int(user_input) < 3:
        print('Invalid input! Try gain...')
