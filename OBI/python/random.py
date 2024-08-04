print('Escreva o valor que deseja: ')
Num = float(input())
print('Escreva a potencia desejada: ')
Pot = int(input())
Zen = Num
if (Pot < 0):
    print('potencia menor que 0, redigite: ')
    Pot = int(input())
else:
    for i in range(Pot - 1):
        Num = Num * Zen
print('Resultado da potencia é: {}'.format(Num))
