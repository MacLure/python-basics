customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
print(customer.get("name"))
print(customer.get("doesnt_exist", "default value of doesn't exist"))

customer["name"] = "rewrite"
customer["birthdate"] = "new data"

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "🙁"
}

for word in words:
    output += emojis.get(word, word) + " "
