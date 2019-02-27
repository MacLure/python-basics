names = ["John", "Bob", "Malcolm", "Sarah", "Mary"]
print(names[0])
print(names[-2])
print(names[2:])
print(names[2:4])
names[0] = "Jon"

numbers = [3, 6, 2, 8, 4, 5, 10, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

numbers.append(20)
numbers.insert(0, 10)
numbers.remove(10)
numbers.pop()
numbers.index(6)
numbers.clear()
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

numbers = (1, 2, 3)
print(numbers[0])

# we cannot update or change tuples.

# unpacking:
coordinates = (1, 2, 3)
x = coordinates[0]
x = coordinates[1]
x = coordinates[2]

# same result:
x, y, z = coordinates

# unpacking can be used on lists as well.