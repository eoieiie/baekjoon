def isitg(word):
    seen = []  # 이미 본 문자를 추적합니다.
    prev_char = ''  # 이전 문자를 저장합니다.
    for char in word:
        if char in seen:  # 이전에 본 문자인 경우
            if char != prev_char:  # 이전 문자와 다르면 그룹 단어가 아닙니다.
                return 0
        else:
            seen.append(char)  # 새 문자를 추가합니다.
            prev_char = char  # 이전 문자를 업데이트합니다.
    return 1  # 모든 검사를 통과하면 그룹 단어입니다.

totalg = 0
cnt = int(input())

for i in range(cnt):
    word = input()
    totalg += isitg(word)

print(totalg)