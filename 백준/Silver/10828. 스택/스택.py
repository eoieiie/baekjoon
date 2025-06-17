import sys

def main() -> None : 
    input = sys.stdin.readline
    n = int(input())

    stack = []
    out_lines = [] #출력값을 한꺼번에 모아서 제출하기

    for _ in range(n) : 
        cmd, *arg = input().split() #개꿀. split으로 받는 인자 중 두번째 인자가 확실하지 않으므로, *arg는 "첫번째 인자를 제외한 나머지를 arg라는 list에 묶어라 라는 뜻임."

        if cmd == 'push':
            stack.append(int(arg[0]))

        elif cmd == 'pop':
            out_lines.append(str(stack.pop() if stack else -1))

        elif cmd == 'size':
            out_lines.append(str(len(stack)))

        elif cmd == 'empty': 
            out_lines.append('0' if stack else '1')

        elif cmd == 'top':
            out_lines.append(str(stack[-1] if stack else -1))

        
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()


# 괄호 짝 검사 (push/ pop 로 매칭)

# DFS 스택 구현 (재귀 대신 스택)

# 문자열 뒤집기 (push(c) → pop)

# 후위 표기식 변환 등
    



    
# 스택 = list는 가장 보편적인 선택 
# 대신 큐 양쪽에서 삭제는 deque

