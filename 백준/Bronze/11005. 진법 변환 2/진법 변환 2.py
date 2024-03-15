a, b = map(int, input().split())
lista = []
con = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:

    result = list(con)[a%b] #리스트 없어도 돼 
    lista.append(result)
    if a < b:
        break
    a //= b

lista.reverse()

for i in lista:
    print(i, end = "")



# n, b = map...
# con = "123..."

# while n:
#     ans += con[n % b]
#     n //= b


# 헤서 [::-1 ]하거나 reverse로 하기. 
