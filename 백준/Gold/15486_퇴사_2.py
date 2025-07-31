import sys

def main() -> None:
    read = sys.stdin.readline
    N = int(read().strip())

    T = [0] * (N + 1)  # 상담 기간 (1-indexed)
    P = [0] * (N + 1)  # 상담 수익

    for i in range(1, N + 1):
        T[i], P[i] = map(int, read().split())

    # dp[i] = i번째 날부터 퇴사일까지 얻을 수 있는 최대
    dp = [0] * (N + 2)           # N+1 ~ N+1까지 접근하는거 대비해서ㅓ

    # 마지막 날부터 역순으로 채우기
    for day in range(N, 0, -1):
        end_day = day + T[day]   # 상담이 끝난 다음 날
        # 상담 불가능(퇴사 후 종료) → 오늘 상담을 못 한다
        if end_day > N + 1:
            dp[day] = dp[day + 1]
        else:
            # ② 상담을 할 때와 안 할 때 중 큰 값을 선택
            do_it   = P[day] + dp[end_day]
            skip_it = dp[day + 1]
            dp[day] = max(do_it, skip_it)

    print(dp[1])                 # 1일 기준 최대 이익 출력

if __name__ == "__main__":
    main()
