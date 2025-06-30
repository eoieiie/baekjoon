import sys

def build_freq(arr):
    # 리스트를 한 번 훑어 값→등장횟수 딕셔너리를 만든다.
    freq = {}
    for x in arr:
      if x in freq:
        freq[x] += 1
      else:
        freq[x] = 1
      
      # freq[x] = freq.get(x, 0) + 1 이렇게 해도 됨. get(x, 0) =x에 해당하는 키값이 없으면 0을 돌려줌, 있으면 그냥 값을 반환. 
    return freq

def main() -> None:
    read = sys.stdin.readline
    n    = int(read())
    nums = list(map(int, read().split()))

    freq  = build_freq(nums)        # Counter 대신 자체 함수
    ans   = [-1] * n
    stack = []                      # 인덱스를 담는 스택

    for i, v in enumerate(nums):
        # 스택 top 원소보다 등장 횟수가 큰 값(v)을 만나면 NGE 확정
        while stack and freq[nums[stack[-1]]] < freq[v]:
            ans[stack.pop()] = v
        stack.append(i)

    sys.stdout.write(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()