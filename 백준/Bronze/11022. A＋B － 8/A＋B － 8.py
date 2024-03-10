amount = int(input())
for i in range(amount):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a + b}")

