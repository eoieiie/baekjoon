alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
word = input().upper()

cnta = 0
for n in alphabet:
    if n in word:
        cnta += 1

lista = [0] * cnta
listb = []
cntb = 0 
cntc = 0

for n in alphabet: #m이 들어감
    if n in word:
        listb.append(n)
        for m in word:#알파벳 다 돌리는데
            if n == m and n not in lista:
                lista[cntb] += 1
        cntb += 1

maxvalue = 0
for i in lista:
    if i > maxvalue:
        maxvalue = i

for i in lista:
    if i == maxvalue:
        cntc += 1

if cntc == 1:
    print(listb[lista.index(maxvalue)])
else:
    print("?")
