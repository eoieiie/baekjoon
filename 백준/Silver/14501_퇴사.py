import sys
read = sys.stdin.readline
N = int(read())
T = [0]*N
P = [0]*N
for i in range(N):
  T[i], P[i] = map(int, read().split())

dp = [0]*(N+1) # i번째 날부터 시작 시 얻을 수 있는 최대 수익, 초기값 0 

for n in range(N-1, -1, -1): #뒤쪽부터
  if n+T[n] <= N: #상담을 할 경우
    dp[n] = max(dp[n+1], dp[n + T[n]] + P[n]) # n+t[n] 이라는 시간이 지나야 상담을 지속 가능함. 그래서 
																							#	현재 수억 pn + 남은날짜에서 얻는 최대 수익을 더함							    
  else: #상담을 하지 않을 경우 
    dp[n] = dp[n+1] # 그냥 다음날로 넘어간다. 


print(dp[0])