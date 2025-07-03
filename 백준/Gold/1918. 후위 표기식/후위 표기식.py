# 피연산자를 만나면 그대로 출력 
# 연산자를 만나면:
#   스택이 비어있지 않고 
#   스택 top의 연산자가 현재보다 같거나 높으면 
#   top을 꺼내 출력 
#   그 뒤에 현재 연산자를 push 

# 왼쪽괄호는 무조건 stackpush 
# 오른쪽 괄호 나올 때까지 스택에서 pop하여 출력, 마지막으로 왼쪽 괄호만 pop해서 버림 

# 핵심 순서는 왼쪽 오른쪽을 유지, 
# 스택에는 아직 자리를 못 잡은 연산자랑 왼쪽 괄호만 잠시 보관


import sys

def main() -> None:

  input = sys.stdin.readline
  operation = list(input().strip())
  temp_stack = []
  answer = []
  #string = "ABCDEFGHIJKLMNOP" 보다 if 'A' <= ch <= 'Z':로 판별하는 게 더 빠름. 

  def priority(op): #연산의 우선순위를 판별하는 함수, 
    return 2 if op in "*/" else 1
  

  for i in operation: #입력된 중위표기 중에서 
    if 'A' <= i <= 'Z': #만약 피연산자라면
      answer.append(i)
    elif i == "(":
      temp_stack.append(i)
    elif i == ")":
      while temp_stack[-1] != "(":
        answer.append(temp_stack.pop())
      temp_stack.pop()

    else: #만약 연산자라면
      while temp_stack and temp_stack[-1] != "(" and priority(temp_stack[-1]) >= priority(i):
        answer.append(temp_stack.pop())
      temp_stack.append(i)

  while temp_stack:
    answer.append(temp_stack.pop())

  sys.stdout.write("".join(answer))

if __name__ == "__main__":
  main()
        