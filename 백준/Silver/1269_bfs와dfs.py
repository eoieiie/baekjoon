# 정점의 개수 
# 간선의 개수 
# 탐색을 시작할 정점의 번호 

# 두 정점 사이에 여러 개의 간선이 있을 수 있음. 
# 입력으로 주어지는 간선은 양방향이다. 




import sys
from collections import deque

read = sys.stdin.readline

# ---------------------
# 입력
#    N : 정점(노드) 개수
#    M : 간선 개수
#    V : 탐색 시작 정점

N, M, V = map(int, read().split())

# 인접한 노드들의 리스트 (1번부터 N번까지 쓰기 위해 N+1 생성)
adj = [[] for _ in range(N + 1)]
# → [[], [], [], [], []]

for _ in range(M):
    a, b = map(int, read().split())
    adj[a].append(b)
    adj[b].append(a)      # 무방향 그래프이므로 양쪽에 모두 추가
                          # 서로 방향을 이어주기. 2차원 리스트이므로 n번째 adj에 m이 들어가는 느낌              

# idx : 내용(예시)
#  0 : []
#  1 : [2, 3, 4]
#  2 : [1, 4]
#  3 : [1, 4]
 # 4 : [1, 2, 3]

# 번호가 작은 정점부터 방문해야 하므로 각 리스트 오름차순 정렬
for lst in adj:
    lst.sort()

# 예시는 이미 오름차순으로 들어감 


# ----------------------
# DFS 재귀

def dfs(start: int) -> list[int]: # 번호를 담은 리스트를 반환하는 것을 나타내는 타입힌트 
    visited = [False] * (N + 1) # 정점 번호가 n으로 끝나므로 인덱스를 그대로 사용하려면 0번째 자리도 핈요함
    order   = []

    def _go(v: int): # 따로 만든 이유는, visited나 order같은 외부 변수를 그대로 사용하기 위해서. 
        visited[v] = True
        order.append(v) # 방문한 순서를 기록
        for nxt in adj[v]: # v랑 연결되어있던 모든 이웃들에 대하여
            if not visited[nxt]: # 그 이웃이 미방문 이웃이라면
                _go(nxt) # 그 친구에 대한 재귀를 호출한다. 
              # 제일 깊은 곳까지 내려갔다면 스택이 백트래킹하며 for문에서 다음 v로 넘어가서(인접한 바로 다음 v) 그 v에 대한 재귀를 시작한다. 

    _go(start)
    return order # 함수는 방문순서를 기록한 int 리스트를 반환한다. 

# ------------------------
# BFS (deque)

# deque를 쓰는 이유:
# 큐의 앞쪽 원소를 꺼내는 popleft()가 O(1)
# list.pop(0)은 O(N)이라 비효율!

def bfs(start: int) -> list[int]: # 
    visited = [False] * (N + 1) #
    q = deque([start]) #큐를 만들어서 탐색시작점을 넣고
    visited[start] = True # 방문여부 표시하고 
    order = [] #방문 순서를 쌓을 결과리스트를 만들고

    while q: #큐가 빌 때까지(한 층씩 넓혀 가기)
        v = q.popleft() #큐 맨 앞에서 꺼낸 수를
        order.append(v) #결과에 넣고 
        for nxt in adj[v]: #그 수와 인접한 수들 중
            if not visited[nxt]: #한번도 안 본 친구들이면
                visited[nxt] = True #방문표시시하고 
                q.append(nxt)# 그 수를 큐에 넣는다
    return order

# ──────────────────────────
# 4) 실행 & 출력
# ──────────────────────────
print(*dfs(V))
print(*bfs(V))
