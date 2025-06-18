import sys

def main() -> None:
    input = sys.stdin.readline
    T = int(input())
    out_lines = []

    for _ in range(T):
        line = input().rstrip('\n') + ' '      # 마지막 단어 처리용 공백
        stack = []
        current = []

        for ch in line:
            if ch != ' ':
                stack.append(ch)
            else:
                while stack:
                    
                    current.append(stack.pop())
                current.append(" ")
        current.pop()
 
        out_lines.append(''.join(current))

    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()
    