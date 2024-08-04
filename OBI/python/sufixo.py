N = int(input('Digite a quantidade de caracteres da primeira palavra: '))

Pi = str(input('Digite a palavra: '))

M = int(input('Digite a quantidade de caracteres da primeira palavra: '))

Si = str(input('Digite a palavra: '))
sufixo = ''
if Si[0] == Pi[0]:
    if M < N:
        Maior = M
    elif N < M:
        Maior = N
    else:
        Maior = M
    for x in range(Maior):
        if Pi[x] == Si[x]:
            sufixo += Pi[x]
    print(f'As duas palavras tem {len(sufixo)} em comum')
else:
    print('Nao tem sufixos em comum!')
