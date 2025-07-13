import sys

def main():
    input = sys.stdin.readline

    ball_pos = 1  # 처음에 1번 컵에 공 있음

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        if ball_pos == a:
            ball_pos = b #옮김
        elif ball_pos == b:
            ball_pos = a
        # 공이 a, b 둘 다 아니라면 굳이 이동 없음

    print(ball_pos)

if __name__ == "__main__":
    main()