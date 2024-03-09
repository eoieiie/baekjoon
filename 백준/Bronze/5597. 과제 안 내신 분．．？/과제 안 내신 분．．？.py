a = list()
for i in range(28):
    a.append(int(input()))

b = list()
for i in range(1, 31):
    if i in a:
        continue
    else:
        b.append(i)
        print(i)


