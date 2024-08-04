#!/usr/bin/env python3

m,n = [int(x) for x in input('Digite').split()]
#inputUser = input('Digite')
#inputSplitado = inputUser.split()
#m = inputSplitado[0]
#n = inputSplitado[1]

# listaCompras = ["feijao", "arroz", "brocolis", "batata"]
# lista = range(1, 10)
# for x in lista:
#     int(x)
# for item in listaCompras:
#     listaCompras[0]
#     print(item)
# print(item)
estoque = []
for i in range(m):
    linha = [int(x) for x in input('Digite').split()]
    estoque.append(linha)

p = int(input('Digite1'))
print(estoque[0][1])
total = 0
for k in range(p):
    i, j = [int(x) for x in input('Digite').split()]
    if estoque[i-1][j-1] > 0:
        estoque[i-1][j-1] -= 1
        total += 1

print(total)

