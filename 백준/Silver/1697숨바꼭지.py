import sys
from collections import deque

MAX_POS = 100_000           # 위치 상한

def bfs_min_time(N: int, K: int) -> int:
    if N >= K:                              # 특수 케이스
        return N - K

    dist = [-1] * (MAX_POS + 1)             # -1 = 미방문
    dist[N] = 0
    q = deque([N])

    while q:
        cur = q.popleft()

        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt <= MAX_POS and dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                if nxt == K:                # 목표에 처음 도달 → 최단
                    return dist[nxt]
                q.append(nxt)

    return dist[K]                          # 이론상 항상 도달 가능

def main() -> None:
    N, K = map(int, sys.stdin.readline().split())
    print(bfs_min_time(N, K))

if __name__ == "__main__":
    main()