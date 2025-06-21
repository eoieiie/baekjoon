import sys

def main() -> None:

    input = sys.stdin.readline
    n = int(input())
    
    stack = [] #입력 담을 곳
    check = [] #n담을 곳
    out = [] # + - 담을 곳
    ok = True #결과 판별용
    temp = 1

    for _ in range(n):
        stack.append(int(input())) #정수면 상관없는데, 문자라면 rstrip 있어야 함

    for i in stack:
        while temp <= i:
            
            #for 문은 자동으로 늘어남. 
            #그래서 while문으로 for문 대신 늘려줄 수 있음. 
            #이게 포인트 
            
            check.append(temp)
            out.append("+")
            temp += 1
        

        if check[-1] == i:
            check.pop()
            out.append("-")

        else:
            ok = False
            break
        

    if ok:
        sys.stdout.write('\n'.join(out))
    else:
        print("NO")

if __name__ == "__main__":
    main()
        
            

        
        

