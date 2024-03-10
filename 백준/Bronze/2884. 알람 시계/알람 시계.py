h, m = map(int, input().split())

inputminute = (h * 60 + m) - 45 #들어온 시간의 총합에서 45분을 뺀 시간 
newh = inputminute // 60
newm = inputminute % 60

if newm >= 60:
    newh += newm // 60
    newm = newm % 60

if newh >= 24:
    newh = newh % 24

if newh < 0:
    newh = newh + 24

print(newh, newm)



