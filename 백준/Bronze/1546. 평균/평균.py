def newscore(a):
    n = max(a)
    cnt = 0
    for i in a:
        i = i / n * 100
        cnt += i
    avg = cnt / len(a)
    return avg




N = int(input())
scorelist = list(map(int, input().split())) #리스트로 감싸는 것이 졸라중요

print(newscore(scorelist))
