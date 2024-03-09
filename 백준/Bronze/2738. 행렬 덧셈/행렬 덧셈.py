# N*M 크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오. 

a = []
b = []

N, M = map(int, input().split())

for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    b.append(list(map(int, input().split())))

for n in range(N):
    for m in range(M):
        print(a[n][m] + b[n][m], end = " ")
    print()
