# Classes are named in capitalized camel-case
# Classes are preceded and followed by 2 line breaks

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.draw()
print(point1.x)
point1.draw()

point2 = Point(11, 23)
point2.x = 1
print(point2.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi, I am {self.name}")


john = Person("John")
john.talk
print(john.name)


# Inheritance:


class Pet:
    def walk(self):
        print("walking...")

class Cat(Pet):
    def be_aloof(selfself):
        print("being aloof...")


class Dog(Pet):
    pass


# Python doesn't like empty classes
# 'pass' has no value, but it can be used to "close" an empty class.

# IMPORTING MODULES

# "input [filename - no extension]" -> in code: [filename, no extension].[function]
# "from [filename - no extension] import [function]
