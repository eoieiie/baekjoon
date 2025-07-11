
#첫 블록 포함 8개의 블록을 흝어야 하므로, 입력된 행 - 7 까지의 범위를 지정해주면 (예: 행이 9개 -> 1~8 이랑 2~9까지 2개의 8자리 범위가 있으므로
#9-7 = 2번 즉 0, 1 해서 총 2번 반복하도록 
#중요한 거: 
#짝짝, 홀홀끼리 같은 색이어야 하고 
#짝홀, 홀짝끼리 같은 색이어야 한다. 
#그래서 두 좌표를 합했을 때 홀수인 경우와 짝수인 경우로 압축해서 생각할 수 있다 

import sys


def main() -> None:

  read = sys.stdin.readline
  n, m = map(int, input().split())
  board = [] #전체 보드를 나타낼 리스트 b
  answer = [] #결과 

  for _ in range(n):
    board.append(read().strip()) 
    
  for i in range(n - 7): #n-7과 m-7범위의 중첩 for문을 작성, 8*8을 만들기 
    for j in range(m - 7):
      draw1 = 0
      draw2 = 0

      for a in range(i, i+8): #이제 8*8 블럭 안에서 인덱스를 판별하기 위해
        for b in range(j, j+8): #행i와 열j를 기준으로 입력받은 보드에 인덱스로 접근한당

          #여기서 첫번쨰 반복은, 첫 블록의 색을 결정하게 된다. B or W가 나오는 것이다!
          #무슨 색이 나오는 지 중요하지는 않다. 단지 무슨 색이 나오든지 그 뒤는 반전색이어야 한다. 
          
          if (a + b) % 2 == 0: #만약 더한 게 짝수(짝짝 or 홀홀)(1, 3...번째 자리)
            if board[a][b] != "B": #그리고 그 좌표가 "B"가 아니라면 즉 시작이 흰색이면 
              draw1 += 1 # d1을칠해준다. 
            if board[a][b] != "W": #만약 시작좌표가 "W"가 아니라면 즉 시작이 검정이면
              draw2 += 1 # d2를칠해준다. 

          else: #만약 더한 게 홀수 (홀짝 or 짝홀)(즉 이제부터는 각 케이스에 맞춤)
            if board[a][b] != "W":
              draw1 += 1
            if board[a][b] != "B" :
              draw2 += 1
              
      answer.append(draw1) #시작이 B인 케이스의 현재 반복문에서의 색칠횟수 
      answer.append(draw2) #시작이 W인 케이스의 색칠횟수
      #를 전체 for문동안 반복하기. 

  print(min(answer)) 

if __name__ == "__main__":
  main()
