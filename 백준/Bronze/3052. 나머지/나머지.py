lista = []
listb = []
cnt = 0

for i in range(10):
    a = int(input())
    lista.append(a)

for n in range(len(lista)):
    b = lista[n] % 42
    lista[n] = b

for i in range(0, 43):
    if i in lista:
        if i not in listb:
            listb.append(i)
            cnt += 1

print(cnt)