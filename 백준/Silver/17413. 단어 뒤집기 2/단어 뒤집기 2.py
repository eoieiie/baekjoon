import sys
input = sys.stdin.readline

def main()-> None:

  #이렇게 자주 쓰일 것 함수는 만들어두고 매번 호출하는 게 좋음.  
  # def flush_word():
  #   if stack:
  #       output.extend(reversed(stack))
  #       stack.clear()


  stack = []
  output = []
  string = input().rstrip()
  inside = False

  # out_append = output.append 이렇게 하면 약간 빨라짐!

  for i in string:

    if i == "<":
      while stack:
        output.append(stack.pop())
      inside = True
      output.append(i)
      
    elif i == ">":
      inside = False
      output.append(i)

    elif inside:
      output.append(i)

    
    #이렇게 해도 됨! 더 가독성이 좋은지는 모르겠지만 다른 if를 할 필요 없이 바로 continue해서 더 빨라짐. 
    # if ch == '<':  
    #   flush_word()
    #   inside = True
    #   output.append(ch)
    #   continue                # 그대로 유지

    # elif inside:                # elif 로 바꿔도 OK
    #   output.append(ch)
    #   if ch == '>':
    #       inside = False
    #   continue

    
      
    elif i == " ":
      while stack:
        output.append(stack.pop())
      output.append(" ")

    else:
      stack.append(i)

  while stack:
    output.append(stack.pop())

  sys.stdout.write("".join(output))

if __name__ == "__main__":
  main()

 
    
      
