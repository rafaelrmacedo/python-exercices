dictionary = {1: 'Gwyn', 2: 'Izalith', 3: 'Nito'}

print(dictionary.get(3))
print(dictionary.get('4', 'None')) # Doesn't exist in dict
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
