import sys
sys.setrecursionlimit(10**6)     # 이전 문제처럼 에러 방지 위해 한도 늘려줌
input = sys.stdin.readline       

T = int(input())                  

# 좌표 이동용
dx = [0, 0, -1, 1]                # x축 (좌우)
dy = [-1, 1, 0, 0]                # y축 (상하)

# DFS
def dfs(x, y):
    visited[y][x] = True         # 방문 처리
    for dir in range(4):        # 4방향 탐색
        nx = x + dx[dir]        # 다음 x
        ny = y + dy[dir]        # 다음 y
        if 0 <= nx < M and 0 <= ny < N:                # 배열 범위 안이면
            if field[ny][nx] == 1 and not visited[ny][nx]:  # 도마도가 있고, 아직 방문 안 한 곳이면
                dfs(nx, ny)     # 그 좌표로 계속 파고듬

# 각 테스트 케이스마다 처리
for _ in range(T):
    M, N, K = map(int, input().split())   # 가로길이, 세로길이, 토마토 수 입력
    field = [[0] * M for _ in range(N)]   # 밭 생성 (2차원 배열, N행 M열)
    visited = [[False] * M for _ in range(N)]  # 방문 여부 배열

    for _ in range(K):                    # K개의 토마토 위치 입력
        x, y = map(int, input().split())  # x: 가로, y: 세로
        field[y][x] = 1                   # 해당 위치에 심기

    worm_count = 0                        # 지렁이 수(= 군집 수) 초기화
    for y in range(N):                    # 전체 밭을 돌며
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:  # 아직 방문 안 했으면
                dfs(x, y)                # DFS로 탐색 시작
                worm_count += 1         # 군집 1개 =지렁이 1마리

    print(worm_count)                    # 출력