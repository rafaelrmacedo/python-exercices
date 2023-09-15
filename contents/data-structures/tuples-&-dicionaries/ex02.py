contats = {}

for i in range(5):
    name = input("Type the name to register: ")
    number = input(f"Tyoe the {name}'s number: :")
    contats[name] = number

print("\n==============Complete Contats==============")
for name, number in contats.items():
    print(f"{name}: {number}")