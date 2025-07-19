import sys

def div_rule(a: int, b: int) -> int:
    return -(-a // b) if a < 0 else a // b

def main() -> None:
    read = sys.stdin.readline

    N    = int(read())
    nums = list(map(int, read().split()))
    plus, minus, mul, div = map(int, read().split())

    max_val = -10**10        # ← main() 스코프
    min_val =  10**10

    def dfs(idx: int, cur: int, p: int, m: int, t: int, d: int):
        nonlocal max_val, min_val   # ← 바로 위(main) 변수를 잡아옴
        if idx == N:
            max_val = max(max_val, cur)
            min_val = min(min_val, cur)
            return

        nxt = nums[idx]
        if p: dfs(idx+1, cur + nxt,         p-1, m,   t,   d)
        if m: dfs(idx+1, cur - nxt,         p,   m-1, t,   d)
        if t: dfs(idx+1, cur * nxt,         p,   m,   t-1, d)
        if d: dfs(idx+1, div_rule(cur,nxt), p,   m,   t,   d-1)

    dfs(1, nums[0], plus, minus, mul, div)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main()