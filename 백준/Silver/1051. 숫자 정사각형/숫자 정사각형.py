N, M = map(int, input().split())
 
d = min(N, M)
 
array = []
for _ in range(N):
    array.append(list(map(int, input())))
 
answer = 1
for i in range(N):
    for j in range(M):
        for k in range(1, d):
            if i + k < N and j + k < M:
                n = array[i][j]
                if n == array[i + k][j] and n == array[i][j + k] and n == array[i + k][j + k]:
                    answer = max(answer, (k + 1) ** 2)
 
print(answer)