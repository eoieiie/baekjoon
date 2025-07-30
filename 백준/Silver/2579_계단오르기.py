import sys

def main() -> None:
    read = sys.stdin.readline

    # 
    n = int(read().strip())                # 계단 수
    stairs = [int(read().strip()) for _ in range(n)]

    # 계단이 1 or 2개인 경우는 규칙을 직접 계산
    if n == 1:
        print(stairs[0])
        return
    if n == 2:
        print(stairs[0] + stairs[1])
        return

    # best[i] = i번째(0‑기준) 계단에 도달했을 때 얻을 수 있는 최대 
    best = [0] * n
    best[0] = stairs[0]                      # 첫 계단
    best[1] = stairs[0] + stairs[1]          # 첫+둘째 계단 (연속 두 칸 허용)

    # 세 번째부터 누적
    for i in range(2, n):
        # 경로 A 전전 계단 → 두 칸
        take_from_two_before = best[i-2] + stairs[i]
        # 경로 B 전전전 계단 → 한 칸 + 한 칸 (전 계단 포함)
        take_from_three_before = best[i-3] + stairs[i-1] + stairs[i]
        # 큰 값을 선택
        best[i] = max(take_from_two_before, take_from_three_before)

    # 마지막 계단 점수
    print(best[-1])

if __name__ == "__main__":
    main()
