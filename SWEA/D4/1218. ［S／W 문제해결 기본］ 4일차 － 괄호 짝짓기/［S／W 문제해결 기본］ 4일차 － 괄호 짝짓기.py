pare = {">": "<", ")": "(", "}": "{", "]": "["}

# 테스트 케이스의 개수
num_test_cases = 10

for tc in range(1, num_test_cases + 1):
    # 테스트 케이스 입력
    length = int(input())
    data = input()

    stack = []
    iscorrect = True

    # 괄호 유효성 검사
    for now in data:
        if now in pare.values():
            stack.append(now)
        elif stack and stack[-1] == pare[now]:
            stack.pop()
        else:
            iscorrect = False
            break

    # 결과 출력
    if not stack and iscorrect:
        print('#%d %d' % (tc, 1))  # 유효한 경우
    else:
        print('#%d %d' % (tc, 0))  # 유효하지 않은 경우
