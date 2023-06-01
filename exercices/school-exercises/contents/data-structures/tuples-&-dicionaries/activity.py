# Faça um sistema de cadastros de agenda telefônica, deve possuir um menu com as seguintes
# opções
# 1 – Inserir
# 2 – Pesquisar
# 3 – Atualizar
# 4 - Mostrar agenda
# 0 - Sair

directory = {}

def insert():
    name = input("Enter name: ")
    if name in directory:
        print("This contact already exists in the directory. \n")
        return
    phone_number = input("Enter phone number: ")
    directory[name] = phone_number
    print("Contact added successfully. \n")

def search():
    name = input("Enter name to search: ")
    if name in directory:
        print(f"Phone number for {name}: {directory[name]}")
    else:
        print("Contact not found. \n")

def update():
    name = input("Enter name to update: ")
    if name not in directory:
        print("Contact not found. \n")
        return
    new_phone_number = input("Enter new phone number: ")
    directory[name] = new_phone_number
    print("Contact updated successfully. \n")

def show_directory():
    print("Directory =>")

    if directory.items() == 0:
        print("Empty directory. \n")
    else:
        for name, phone_number in directory.items():
            print(f"{name}: {phone_number}")

while True:
    print("Menu:\n1 - Insert\n2 - Search\n3 - Update\n4 - Show directory\n0 - Exit")
    option = input("Choose an option: ")
    if option == "1":
        insert()
    elif option == "2":
        search()
    elif option == "3":
        update()
    elif option == "4":
        show_directory()
    elif option == "0":
        break
    else:
        print("Invalid option. Please try again. \n")