N = int(input())
a =[0] * N

for i in range(N):
    a[i] = list(map(str, input().split()))

for i in range(N):
    for l in a[i][1]:
        print(l * int(a[i][0]), end = "")
    print()