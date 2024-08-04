m = int(input())
n = int(input())
i = 0
Cx = 0
x = 0
estoque = []
total = []
Quant = 0

for i in range(m * n):
    Cx += 1
    x = int(input())
    total.append(x)
    if Cx == n:
        estoque.append(total)
        total = []
        Cx = 0

Pedidos = int(input())
Pedido = 0

for s in range(Pedidos):
    tamanho = int(input())
    tipo = int(input())
    if estoque[tamanho - 1][tipo - 1] > 0:
        estoque[tamanho - 1][tipo - 1] -= 1
        Quant += 1
print(Quant)

    
