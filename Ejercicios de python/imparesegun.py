list = []

list2 = []
numero = int(input())

for i in range(numero):
    numero = int(input())
    list.append(i)
    indice = list.index(i)
    if indice%2!=0 and indice!=0:
        list2.append(numero)

for j in list2:    
    print(j)