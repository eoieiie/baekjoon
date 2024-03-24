m,n = map(int,input().split())
dic = {}
for _ in range(m):
	a,b = input().split()
	dic[a] = b
for _ in range(n):
	addr = input()
	print(dic[addr])
