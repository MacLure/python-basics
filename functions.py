def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


# functions should be preceded and followed by 2 empty lines

print("Start")
print("Finish")

# Positional arguments:
greet_user("Malcolm", "Maclure")

# Keyword arguments:
greet_user(last_name="Maclure", first_name="Malcolm")

# Keyword arguments should occur after positional arguments


def square(number):
    return number * number


result = square(3)
print(result)
print(square(4))


def print_only():
    print("something, but not returning it")
    return None


print_only()


def emoji_converter(txt):
    words = txt.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "🙁"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = "good morning :)"
print(emoji_converter(message))

# Handling errors:

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")

# Exit code 0 = program didn't crash
# Exit code 1 = program crashed
