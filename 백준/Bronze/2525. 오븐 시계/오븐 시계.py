def finaltime(a, b, c):
    addtime = c // 60

    if a >= 24:
        a = a - 24

    b = b + c
    if b >= 60:
        a = a + (b // 60)
        b = b % 60

    if a >= 24:
        a = a - 24

    return a, b

hour, minute = map(int, input().split())
eta = int(input())

result = finaltime(hour, minute, eta)

for i in result:
    print(int(i), end=" ")
