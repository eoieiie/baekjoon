
import sys
from collections import deque

MAX = 100_000  # 위치의 유효 범위: 0 ~ 100000

def solve(N: int, K: int) -> tuple[int, int]:
    """
    dist[x]  : 위치 x에 도달하는 '최단 시간'
    ways[x]  : 위치 x에 '최단 시간으로' 도달하는 '방법 수'
    BFS로 탐색하면서, 같은 최단 깊이로 재도달하면 ways늘리깅
    """

    # (특수케이스)N >= K이면 뒤로 걷기만 하는 것이 최단(시간 = N-K) 방법 1가지
    if N >= K:
        return N - K, 1

    dist = [-1] * (MAX + 1)   # -1은 미방문
    ways = [0]  * (MAX + 1)   # 방법 수 카운터

    dist[N] = 0              # 시작점까지의 시간은 0
    ways[N] = 1            # 시작점에 도달하는 방법은 1가지(그대로 시작)
    q = deque([N])     # BFS 초기화

    while q:
        cur = q.popleft()

        # 이동 연산 3개 
        for nxt in (cur - 1, cur + 1, cur * 2):
            if 0 <= nxt <= MAX:
                if dist[nxt] == -1:
                    # 첫 방문 최단 시간 정하기( 방법 수는 현재 노드의 방법 수와ㅗㄷㅇ잉ㄹ)
                    dist[nxt] = dist[cur] + 1
                    ways[nxt] = ways[cur]
                    q.append(nxt)
                elif dist[nxt] == dist[cur] + 1:
                    # 이미 방문했지만 또까튼 최단 시간으로 또 도달했다면
                    # 최단 경로가 추가로 발견된 것이므로 방법 수 추가
                    ways[nxt] += ways[cur]

    # K에 대한 최단 시간과 그 시간으로 가는 방법 수 반환
    return dist[K], ways[K]

def main() -> None:
    # 입력: N(수빈 위치), K(동생 위치)
    N, K = map(int, sys.stdin.readline().split())

    # 풀이 실행
    t, cnt = solve(N, K)

    # 출력 형식: 첫 줄 최단 시간, 둘째 줄 최단 방법 수
    print(t)
    print(cnt)

if __name__ == "__main__":
    main()