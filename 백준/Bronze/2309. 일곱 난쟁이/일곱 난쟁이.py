import sys

def main() -> None:

    read = sys.stdin.readline
    stack = [] #판별용 스택

    ages = [int(read()) for _ in range(9)]     #나이넣어줌
    extra_age = sum(ages) - 100                #9명분의 나이 - 100 = a

    for age in ages: #순서대로 나이를 흝는데, 

        another_age = extra_age - age

        if stack and another_age in stack: #스택에 무엇인가가 들어있고,
                                           #그 수들 중 현재 n과 더해서 엑스트라 나이가 나오는 조합이 있다면
            ages.remove(age)
            ages.remove(another_age)
            break # 하나 찾으면 즉시 종료

        else:
            stack.append(age)

    ages.sort()
    sys.stdout.write("\n".join(map(str, ages))) 

if __name__ == "__main__":
    main()