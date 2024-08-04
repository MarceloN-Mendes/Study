a = int(input())
b = int(input())
Sa = []
SaADD = 0
Sb = []
SbADD = 0
i = 0
j = 0
resp = 'S'

for x in range(a):
    SaADD = str(input())
    Sa.append(SaADD) 

for y in range(b):
    SbADD = str(input())
    Sb.append(SbADD)
    
while True:
    if Sa[i] == Sb[j]:
        i +=1
        j +=1
    else:
        i +=1
    
    if j == b:
        break
    if i == a:
        resp = 'N'
        break
print(resp)