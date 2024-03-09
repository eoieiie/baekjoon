a = int(input())
b = a


if a == 0:
    print(1)

else:
    for i in range(1, a):
        b *= (a - i)
        a - 1

    print(b)