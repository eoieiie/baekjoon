import sys

MOD = 10007  # 문제에서 요구한 나머지(나눌거)

def main() -> None:
    read = sys.stdin.readline
    n = int(read().strip())  # 직사각형 세로 길이

    # 세로 길이가 1일 때는 방법이 1가지
    if n == 1:
        print(1)
        return

    #ways[i] = 세로 길이가 i일 때 방법 수 (1‑기준)
    ways = [0] * (n + 1)
    ways[1] = 1      # 2×1 = 세로 타일 하나
    ways[2] = 2      # 2×2 = 세로+세로, 가로2개

    # ways[i] = ways[i‑1] + ways[i‑2]  
    for i in range(3, n + 1):
        ways[i] = (ways[i - 1] + ways[i - 2]) % MOD

    print(ways[n])

if __name__ == "__main__":
    main()
