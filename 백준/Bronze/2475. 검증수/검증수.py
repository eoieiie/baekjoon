nums = input().split()

a = 0

for i in nums:
    i = int(i)
    a += i * i 

isit = a % 10
print(isit)

