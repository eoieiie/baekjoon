def findindex(a):

    listascii = []
    listword = []
    listreturn = []

    for i in range(abs(ord("a") -  ord("z"))+1):
        listascii.append(97 + i)

    for i in a:
        listword.append(ord(i))

    for n in listascii:
        if n in listword:
            listreturn.append(listword.index(n))
        else:
            listreturn.append(-1)

    return listreturn


word = input()

for i in findindex(word):
    print(i, end = " ")
