#5
data = input()
phone_numbers = {}

while data != "Over":
    name = data.split(":")[0].strip()
    number = data.split(":")[1].strip()

    if number.isnumeric():
        phone_numbers[name] = number
    else:
        phone_numbers[number] = name
    data = input()

for kvp in sorted(phone_numbers.items()):
    print(f"{kvp[0]} -> {kvp[1]}")