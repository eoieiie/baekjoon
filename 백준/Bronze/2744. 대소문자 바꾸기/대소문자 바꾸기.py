word = input()

for i in word:
    if ord("A") <= ord(i) <= ord("Z"):
        print(i.lower(), end = "")
    elif ord("a") <= ord(i) <= ord("z"):
        print(i.upper(), end = "")

