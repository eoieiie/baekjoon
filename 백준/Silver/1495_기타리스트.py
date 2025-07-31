import sys

def main() -> None:
    read = sys.stdin.readline
    n, s, m = map(int, read().split())
    diffs = list(map(int, read().split()))  # 볼륨 변화폭 V[0..n-1]

    # 현재 단계에서 가능한 음량 표시용
    possible = [False] * (m + 1)
    possible[s] = True  # 시작

    for diff in diffs:               # 곡을 순서대로 처리
        next_possible = [False] * (m + 1)
        for vol in range(m + 1):     # 0..M 전부 스캔
            if not possible[vol]:
                continue
            # +diff
            if vol + diff <= m:
                next_possible[vol + diff] = True
            # -diff
            if vol - diff >= 0:
                next_possible[vol - diff] = True
        possible = next_possible     # 다음 곡으로

    # 결과!
    for vol in range(m, -1, -1):     # 최댓값부터 뒤져서 찾기
        if possible[vol]:
            print(vol)
            return
    print(-1)                        # 하나도 못 찾음~

if __name__ == "__main__":
    main()
