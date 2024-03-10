givenprice = int(input())
quan = int(input())

datalist = []
finalprice = 0

for i in range(quan):
    price, eachquan = list(map(int, input().split()))
    datalist.append((price, eachquan)) #append는 하나의 요소만 리스트에 추가 가능. 


for i in range(quan):
    finalprice += datalist[i][0] * datalist[i][1]

if givenprice == finalprice:
    print("Yes")
else:
    print("No")


