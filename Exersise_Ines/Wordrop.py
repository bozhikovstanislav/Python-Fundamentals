
n = int(input())
wardrobe = {}

for _ in range(n):
    data = input()
    color = data.split(" -> ")[0]
    clothes_items_list = data.split(" -> ")[1].split(",")

    if not color in wardrobe.keys():
        wardrobe[color] = {}
        for item in clothes_items_list:
            if not item in wardrobe[color].keys():
                wardrobe[color][item] = 1
            else:
                wardrobe[color][item] += 1
    else:
        for item in clothes_items_list:
            if not item in wardrobe[color].keys():
                wardrobe[color][item] = 1
            else:
                wardrobe[color][item] += 1

data = input()
color_wanted = data.split()[0]
item_wanted = data.split()[1]

for color in wardrobe:
    print(f'{color} clothes:')
    for item in wardrobe[color]:
        if color_wanted == color and item_wanted == item:
            print(f'* {item} - {wardrobe[color][item]} (found!)')
        else:
            print(f'* {item} - {wardrobe[color][item]}')