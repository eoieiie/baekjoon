word = input()
totalcount = 0

for idx, char in enumerate(word):
    if char == "c":
        if idx + 1 < len(word) and (word[idx + 1] == "=" or word[idx + 1] == "-"):
            totalcount -= 1
    elif char == "d":
        if idx + 2 < len(word) and word[idx + 1] == "z" and word[idx + 2] == "=":
            totalcount -= 1
        elif idx + 1 < len(word) and word[idx + 1] == "-":
            totalcount -= 1
    elif char in ["l", "n"]:
        if idx + 1 < len(word) and (word[idx + 1] == "j"):
            totalcount -= 1
    elif char in ["s", "z"]:
        if idx + 1 < len(word) and (word[idx + 1] == "="):
            totalcount -= 1
    
    totalcount += 1

print(totalcount)
