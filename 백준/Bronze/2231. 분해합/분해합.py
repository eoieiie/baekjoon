import sys

def main() -> None:
    read = sys.stdin.readline
    n = int(read().strip())

    # 최적화: n - 9*len(str(n))부터 검사 시작 (최소 가능한 생성자)
    start = max(1, n - 9 * len(str(n)))

    for i in range(start, n):
        digit_sum = i + sum(int(d) for d in str(i))
        if digit_sum == n:
            print(i)
            return

    print(0) 

if __name__ == "__main__":
    main()
