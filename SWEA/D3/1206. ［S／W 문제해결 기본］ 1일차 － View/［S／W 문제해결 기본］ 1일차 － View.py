def maxsideindex(lista, indx):
    maxval = max(lista[indx-2], lista[indx-1], lista[indx+1], lista[indx+2])
    return maxval

for i in range(10):

    totaljomang = 0

    howmany = int(input())
    lista = list(map(int, input().split()))

    for where, buildingindex in enumerate(lista): 
        if buildingindex == 0:
            continue
        else:
            temp = buildingindex - maxsideindex(lista, where)
            if temp < 0:
                continue
            else:
                totaljomang += temp

    print(f"#{i+1} {totaljomang}")

