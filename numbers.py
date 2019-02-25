print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

X = 10
X += 3
print(X)

y = 2.9
print(round(y))
print(abs(-2.9))

print("Python3 math module")
import math

print(math.floor(2.9))
print(math.ceil(2.9))

is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's a lovely day.")
print("Enjoy your day.")

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligable for loan")

if has_high_income or has_good_credit:
    print("Eligable for loan")

if has_good_credit and not has_criminal_record:
    print("Eligable for loan")

temperature = 35

if temperature == 30:
    print ("it's 30 degrees")

if temperature != 30:
    print ("it's not 30 degrees")

if temperature <= 30:
    print("it's less than 30 degrees")

if temperature >= 30:
    print("it's more than 30 degrees")