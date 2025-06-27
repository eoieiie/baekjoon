import sys

def main() -> None:
    input = sys.stdin.readline
    sticks = input().rstrip()

    stack = []         # ← temp → stack 으로 좀 더 직관적으로
    count = 0
    laser = False      # 직전에 본 문자가 '(' 인지 기억하는 플래그

    def increase():
        nonlocal count
        count += len(stack)   # 레이저 자르기: 현재 막대 수만큼 +=

    for ch in sticks:
        if ch == '(':                 # 막대 시작 또는 레이저 시작
            stack.append('(')
            laser = True              # 다음 문자가 ')' 이면 레이저로 판정
        else:  # ch == ')'
            stack.pop()               # 어쨌든 '(' 하나는 사라짐
            if laser:                 # 직전 문자가 '(' → 레이저
                increase()
            else:                     # 레이저가 아닌 단순 막대 끝
                count += 1
            laser = False             # 이번에 ')' 를 봤으니 다음엔 레이저 아님

    print(count)

if __name__ == "__main__":
    main()