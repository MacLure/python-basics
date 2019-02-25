print('Malcolm MacLure')
print("o----")
print(' ||||')
print('*' * 10)

price = 10
rating = 4.9
name = "Malcolm"
is_published = True

print(price)

name = input("What is your name? ")
print("Hi " + name)
fav_color = input("What color do you like? ")
print(name + " likes " + fav_color)
print("first letter is " + name[0])
print("next 3 letters: " + name[1:4])
print("first 5 letters: " + name[:5])
print("last letters after the 5th: " + name[5:])

birth_year = input('Birth year: ')
age = 2019 - int(birth_year)
print(type(age))
print(age)

multiline_string = '''Hello,

This is a miltiline
string.'''

print (multiline_string)

msg = f'{name} likes {color}.'
print(msg)

string_length = len(name)
print(string_length)
print(name.upper())
print(multiline_string.find('llo'))
print(multiline_string.find('x'))
print(multiline_string.replace('Hello', 'hey hey'))
print('multiline' in multiline_string)