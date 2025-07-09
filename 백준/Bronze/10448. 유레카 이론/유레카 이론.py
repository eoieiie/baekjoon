import sys

def main() -> None:

  read = sys.stdin.readline
  n = int(read())

  stack = [int(read()) for _ in range(n)] #판별할 수 집어넣기 
  triangle_stack = [] #삼각수 목록을 넣을 스택 
  answer = [] #결과입력용 answer

  def triangle(no): #자연수 no의 삼각수를 반환
    return ((no+1)*no)//2

  # 삼각수 목록 만들기 (max input = 1000이라고 문제에서 줌)
  start = 1
  while triangle(start) <= 1000:
    triangle_stack.append(triangle(start))
    start += 1

  for number in stack: # 하나씩 판별시작
    found = False # break 판별용

    # 삼중포문으로 하나씩 다 체크 
    for i in triangle_stack:
      if found: #
        break #세번째 탈출
      for j in triangle_stack:
        if found:
          break #두번째 탈출
        for k in triangle_stack:
          if i + j + k == number:
            answer.append(1)
            found = True
            break #첫번째 탈출

    if not found:
      answer.append(0)

  sys.stdout.write("\n".join(map(str, answer)))

if __name__ == "__main__":
  main()
