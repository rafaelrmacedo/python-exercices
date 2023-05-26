list = ['solaire', 'gwyn']
print(list[1])

list.pop()
print(list)

#Percorrer a lista
list.append('Taurus Demon')

for count in list:
    print(count)

for count in range(0, len(list)):
    print(f"Indice {count} está {list[count]}")

#"Linkar" uma lista na outra
list2 = list
print(list2)
list.append('Artorias')
print(list2)

#Copiando
list2 = list.copy()
print(list2)
list2.pop()
print(list2)

#Concatenação
list3 = ['Gwynevere']
list4 = list + list2 + list3
print(list4)

#Matriz
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for count in matrix:
    for count2 in count:
        print(count2)

