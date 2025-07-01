import sys
input = sys.stdin.readline

n       = int(input()) #수 개수
postfix = input().strip() #후위표기
values  = [float(input()) for _ in range(n)] #n만큼 수를 받아 넣는다([0]부터 차례대로)
table   = {chr(ord('A')+i): values[i] for i in range(n)}  # 매핑, i는 0부터 시작해서 ord(유니코드정수변환) 이후 다시 chr(정수를문자로변환) 하여 반복문을 활용해 각 문자에 value들을 매핑시킨다. 
# table = {문자:숫자} 식으로 바뀜. 잘 기억해두기. 

stack = []

for ch in postfix:
    if 'A' <= ch <= 'Z':            #를 활용해서
        stack.append(table[ch]) # 스택에다가 수 넣기 
    else:                           
        b = stack.pop()
        a = stack.pop()
        if   ch == '+':
            stack.append(a + b)
        elif ch == '-': 
            stack.append(a - b)
        elif ch == '*': 
            stack.append(a * b)
        else:           
            stack.append(a / b)

print(f'{stack.pop():.2f}')