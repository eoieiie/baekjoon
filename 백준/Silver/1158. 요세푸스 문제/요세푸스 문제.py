import sys
from collections import deque

read = sys.stdin.readline
N, K = map(int, read().split())

dq = deque(range(1, N + 1))
answer = []

while dq:
    # K-1 번 앞사람을 뒤로 보낸다
    for _ in range(K - 1):
        dq.append(dq.popleft())   # popleft → append

    answer.append(str(dq.popleft()))  # K번째 제거

print('<' + ', '.join(answer) + '>')




#for 문 대신에 

#dq.rotate(-(k - 1)) 넣으면 너무 쉬움. 사용법은 
#from collections import deque

#dq = deque([1, 2, 3, 4, 5])
#dq.rotate(2)     # 시계방향으로 2칸
#print(dq)        # deque([4, 5, 1, 2, 3])

#dq.rotate(-3)    # 반시계(-)로 3칸
#print(dq)        # deque([2, 3, 4, 5, 1])
