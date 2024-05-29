import sys
input = sys.stdin.readline

def updatefen(i):
  while i<=M:
    fen[i] += 1
    i += i&-i

def sumfen(i):
  SUM = 0
  while i:
    SUM += fen[i]
    i -= i&-i
  return SUM

N = int(input()); M = 1<<19
data = sorted([(int(input()),i) for i in range(1,N+1)],reverse=True)

fen = [0]*(M+1); result = [0]*N
for x,i in data:
  result[i-1] = sumfen(i-1)+1
  updatefen(i)

print(*result,sep="\n")