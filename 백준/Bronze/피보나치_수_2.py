import sys
n = int(sys.stdin.readline())

def fib(x: int) -> int:
    if x < 2:
        return x
    a, b = 0, 1
    for _ in range(2, x+1):
        a, b = b, a + b
    return b

print(fib(n))