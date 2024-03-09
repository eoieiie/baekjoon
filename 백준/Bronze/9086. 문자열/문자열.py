# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오. 


lst = []
cnt = int(input())

for i in range(cnt):
    lst.append(list(input()))

for i in range(cnt):
    print(lst[i][0]+lst[i][len(lst[i])-1])





