'''
06.Exam Shopping
A supermarket has products which have quantities. Your task is to stock the shop before Exam Sunday. Until you receive
the command “shopping time”, add the various products to the shop’s inventory, keeping track of their quantity (for inventory purposes).
When you receive the aforementioned command, the students start pouring in before the exam and buy various products.
The format for stocking a product is: “stock {product} {quantity}”.
The format for buying a product is: “buy {product} {quantity}”.
If a student tries to buy a product, which doesn’t exist, print “{product} doesn't exist”.
 If it does exist, but it’s out of stock, print “{product} out of stock”. If a student tries buying more than the quantity of that product,
  sell them all the quantity of the product (the product is left out of stock, don’t print anything).
When you receive the command “exam time”, your task is to print the remaining inventory in the following format:
 “{product} -> {quantity}”. If a product is out of stock, do not print it.

stock Boca_Cola 10
stock Boca_Cola 10
exam time
'''

shoping_store = {}
inventory_list = []

while True:
    start_stocking = list(input().split(' '))
    if start_stocking[0] + ' ' + start_stocking[1] == 'shopping time':
        break
    elif start_stocking[0] == 'stock':
        if start_stocking[1] in shoping_store:
            shoping_store[start_stocking[1]] = int(start_stocking[2]) + shoping_store.get(start_stocking[1], 0)
        else:
            shoping_store[start_stocking[1]] = int(start_stocking[2])

while True:
    buy_product = list(input().split(' '))
    if buy_product[0] + ' ' + buy_product[1] == 'exam time':
        break
    elif buy_product[0] == 'buy':
        if buy_product[1] in shoping_store:
            shoping_store[buy_product[1]] = shoping_store.get(buy_product[1], 0) - int(buy_product[2])
        elif buy_product[1] in shoping_store and buy_product[2] > shoping_store.get(buy_product[1]):
            shoping_store[buy_product[1]] = shoping_store.get(buy_product[1], 0) - int(buy_product[1])
        elif not buy_product[1] in shoping_store:
            inventory_list.append(f"{buy_product[1]} doesn't exist")
        elif buy_product[1] in shoping_store and buy_product[2] == 0:
            inventory_list.append(f"{buy_product[1]} out of stock")

print("\n".join([inventory_list[x] for x in range(0, len(inventory_list))]))
for k, v in shoping_store.items():
    if v > 0:
        print(f'{k} -> {v}')
