n = int(input())

for i in range(n):
    print(f"{(' ' * (n - i - 1))}{'*' * (i*2+1)}")

for i in range(1, n):
    print(f"{(' ' * i)}{('*' * ((2 * (n-i))- 1))}")





