#6
data = input()
inventory = {}


while data != "shopping time":
    stock = data.split()[1]
    quantity = data.split()[2]

    if stock in inventory.keys():
        inventory[stock] += int(quantity)
    else:
        inventory[stock] = int(quantity)


    data = input()

data = input()

while data != "exam time":
    product = data.split()[1]
    required_quantity = data.split()[2]

    if product in inventory.keys():
        if int(inventory[product]) <= 0:
            print(f"{product} out of stock")
        else:
            inventory[product] -= int(required_quantity)
    else:
        print(f"{product} doesn't exist")
    data = input()

for item in inventory.items():
    if item[1] <= 0:
        continue
    print(f"{item[0]} -> {item[1]}")