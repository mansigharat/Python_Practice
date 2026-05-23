items = ['pen', 'notebook', 'bag']
prices = [10, 45, 120]

for items, prices in zip(items, prices):
    print(f'{items}:{prices}')