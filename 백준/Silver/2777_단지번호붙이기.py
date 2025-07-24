import sys
from collections import deque

def main() -> None:
    read = sys.stdin.readline
    N = int(read().strip())
    grid = [list(map(int, read().strip())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]
    counts = []

    # 상, 하, 좌, 우
    DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def dfs_iter(sy: int, sx: int) -> int:
        
        stack = [(sy, sx)]
        visited[sy][sx] = True
        cnt = 0

        while stack:
            y, x = stack.pop()
            cnt += 1
            for dy, dx in DIRS:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx] and grid[ny][nx] == 1:
                        visited[ny][nx] = True
                        stack.append((ny, nx))
        return cnt

    # 모든 칸을 돌며 새 단지를 발견할 때마다 DFS 실행
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1 and not visited[y][x]:
                counts.append(dfs_iter(y, x))

    counts.sort()

    print(len(counts))
    for c in counts:
        print(c)

if __name__ == "__main__":
    main()