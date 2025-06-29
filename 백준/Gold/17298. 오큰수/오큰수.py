import sys

def main() -> None:

  input = sys.stdin.readline
  n = int(input())
  nums = list(map(int, input().split()))
  ans = [-1] * n
  stack = []

  for i, v in enumerate(nums):
    while stack and nums[stack[-1]] < v:
      ans[stack.pop()] = v

    stack.append(i)


  sys.stdout.write(' '.join(map(str, ans))) # int라서!

if __name__ == "__main__":
    main()
