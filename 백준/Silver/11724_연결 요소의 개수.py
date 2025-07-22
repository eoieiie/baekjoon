import sys
sys.setrecursionlimit(10**6)  
input = sys.stdin.readline

N, M = map(int, input().split())  # 정점 N, 간선 M
adj = [[] for _ in range(N + 1)]  # 인접한거
visited = [False] * (N + 1)       # 방문했나

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# DFS 정의
def dfs(v):
    visited[v] = True
    for nxt in adj[v]:
        if not visited[nxt]:
            dfs(nxt)

# 연결 요소 개수 세기
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
