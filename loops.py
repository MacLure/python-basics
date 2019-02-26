i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

secret_number= 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed.")

command= ""
started = False
while True:
    command = input(">").lower()
    if command =="start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that.")

for item in range(10):
    print(item)

for number in range(5, 10, 2):
    print(f"starts at 5, ends before 10, counts by 2 {number}")

for letter in "Python":
    print(letter)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(total)

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for Counter in range(number):
        output += "X"
    print(output)

