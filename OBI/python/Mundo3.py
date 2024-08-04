E, M, D = [int(x) for x in input().split()]
Q = [] 
A = []
S = [] 
Z = [] 
G = [] 
B = []
F= 0
for x in range(M):
    X, Y = [int(x) for x in input().split()]
    Q += X, Y
    A.append(Q)
    Q = []
for x in range(D):
    U, V = [int(x) for x in input().split()]
    Z += U, V
    S.append(Z)
    Z = []
for x in range(E // 3):
    I, J, K = [int(x) for x in input().split()]
    G += I, J, K
    B.append(G)
    G = []
for x in B:
    for i in S:    
        if i in x:
            F += 1
    for h in A:
        if h not in x:
            F += 1
print(F)
