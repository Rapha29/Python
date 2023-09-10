for i in range(0, 10):
    print(i)
    i = i+1
else:
    print('Fim loop')

--------------------------------

list1 = ['Maca', 'Banana', 'Melao']
list2 = ['Tomate', 'Cebola', 'Cenora']

-------------------------------

for i, j in zip(list1, list2):
    print(i, j)

    ------------------------

for i,j in enumerate(list2):
    print(i, j)


-----------------------------

contador = 0
while contador <= 5:
    print("Contador:", contador)
    contador += 1