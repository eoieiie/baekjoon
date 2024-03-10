N, M = map(int, input().split())
basket = [0] * N

for i in range(N):
    basket[i] = i+1

for i in range(M):
    a, b = map(int, input().split()) # 1, 2

    n = basket[a - 1]
    basket[a - 1] = basket[b - 1]
    basket[b - 1] = n

for i in range(len(basket)):
    print(basket[i], end = " ")
