def calculateprice(a, b, c):
    if a == b == c:
        return 10000 + a*1000
    elif a == b or a == c or c == b:
        if a == b:
            return 1000 + a*100
        if a == c:
            return 1000 + a*100
        if c == b:
            return 1000 + c*100
    else:
        max = a
        if b > max:
            max = b
        if c > max:
            max = c 

        return max * 100




a, b, c = map(int, input().split())

print(calculateprice(a, b, c))
