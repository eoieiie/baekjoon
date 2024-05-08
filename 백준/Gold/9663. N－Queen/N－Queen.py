def solve_n_queens(n):
    # 퀸을 배치하는 함수
    def place_queens(row):
        nonlocal ans
        if row > n:
            ans += 1
            return
        
        for col in range(1, n+1):
            if not visitedx[col] and not visitedIncrease[row + col] and not visitedDEcrease[row - col + n]:
                visitedx[col] = visitedIncrease[row + col] = visitedDEcrease[row - col + n] = 1
                place_queens(row + 1)
                visitedx[col] = visitedIncrease[row + col] = visitedDEcrease[row - col + n] = 0

    # 초기화
    ans = 0
    visitedx = [0] * (n + 1)
    visitedIncrease = [0] * (2 * n + 1)
    visitedDEcrease = [0] * (2 * n + 1)

    # 퀸 배치 시작
    place_queens(1)

    return ans

# 입력 받기
N = int(input())

# 퀸을 놓는 방법의 수 출력
print(solve_n_queens(N))
