#스택은 총 2개로 나누어서 생각해야 한다. 
#커서를 기준으로 왼쪽과 오른쪽을 나누어서 생각해야 한다.
#커서 오른쪽에 있는 애들을 temp_stack에 넣고 
#커서 왼쪽에서는 append나 pop으로 수정한다. 
#커서의 오른쪽에는 글자를 남겨두지 않는다.

import sys

def main() -> None:
  input = sys.stdin.readline

  stack = list(input().rstrip())
  temp_stack = []

  #이것보다 left right 처럼 적는 게 더 직관적임
  #항상 직관적인 변수명을 고민하자. 쉬운 게 장땡이다
  
  n = int(input())

  for _ in range(n):

    op, *args = input().split()
    
    if op == "L" and stack:
      temp_stack.append(stack.pop())
           
    elif op == "D" and temp_stack:
      stack.append(temp_stack.pop())
      
    elif op == "B" and stack:
      stack.pop()
      
    elif op == "P":
      stack.append(args[0])

    else:
      continue

  while temp_stack:
    stack.append(temp_stack.pop())

  #또는 stack.extend(reversed(temp_stack))
    



  sys.stdout.write("".join(stack))

if __name__ == "__main__":
  main()
      