correct = [1, 1, 2, 2, 2, 8]

wrong = list(map(int, input().split()))


cnt = 0

for m in wrong:
    if m <= correct[cnt]:
        print(abs(correct[cnt]-m), end = " ")
    elif m >= correct[cnt]:
        print(-abs(correct[cnt]-m), end = " ")
    cnt += 1
    
