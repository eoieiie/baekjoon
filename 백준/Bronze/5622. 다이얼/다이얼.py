wordlist = (("ABC"),("DEF"),("GHI"),("JKL"),("MNO"),("PQRS"),("TUV"),("WXYZ"))

word = input()
time = 0
for n in word:
    cnt = 3
    for m in wordlist:
        if n in m:
            time += cnt
        else:
            cnt += 1

print(time)
