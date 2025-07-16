# clean_bingo.py
import sys

def main() -> None:
    read = sys.stdin.readline           # 빠른 입력

    # ───────────────────────────
    # 1) 5×5 빙고판 읽기 & 좌표 사전 구축
    board = [list(map(int, read().split())) for _ in range(5)]
    loc = {num: (r, c)                  # {값: (행, 열)}
           for r, row in enumerate(board)
           for c, num in enumerate(row)}

    # ───────────────────────────
    # 2) 사회자가 부르는 25개 숫자 읽기
    calls = [n for _ in range(5) for n in map(int, read().split())]

    # ───────────────────────────
    # 3) 행·열·대각선 카운터
    row_cnt = [0] * 5
    col_cnt = [0] * 5
    diag_cnt = [0, 0]        # [↘, ↗]
    finished = set()         # 이미 완성된 줄들
    bingo = 0

    # ───────────────────────────
    # 4) 한 숫자씩 소화
    for turn, num in enumerate(calls, start=1):
        r, c = loc[num]
        row_cnt[r] += 1
        col_cnt[c] += 1
        if r == c:         # ↘
            diag_cnt[0] += 1
        if r + c == 4:     # ↗
            diag_cnt[1] += 1

        # 막 채워진 칸이 포함된 줄만 검사
        if row_cnt[r] == 5 and ('row', r) not in finished:
            bingo += 1; finished.add(('row', r))
        if col_cnt[c] == 5 and ('col', c) not in finished:
            bingo += 1; finished.add(('col', c))
        if r == c and diag_cnt[0] == 5 and 'diag0' not in finished:
            bingo += 1; finished.add('diag0')
        if r + c == 4 and diag_cnt[1] == 5 and 'diag1' not in finished:
            bingo += 1; finished.add('diag1')

        if bingo >= 3:      # 세 줄 이상이면 종료
            print(turn)
            return

if __name__ == "__main__":
    main()