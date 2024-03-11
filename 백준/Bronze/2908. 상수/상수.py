def changeword(a):
    lista = []
    for i in str(a):
        lista.append(i)

    lista.reverse()
    return lista

a, b = map(int, input().split())

a = changeword(a)
b = changeword(b)

if a > b:
    for i in a:
        print(i, end = "")

else:
    for i in b:
        print(i, end = "")
