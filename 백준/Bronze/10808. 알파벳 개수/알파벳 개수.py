# a 에서 z까지 0을 할당한 스택을 하나 만들고, 
# 매핑으로 각 알파벳에 인덱스를 할당하고, 
# 특정 알파벳이 나올 때마다 해당 알파벳의 인덱스에 해당하는 
# 스택의 자리에 +1을 해줄거다


#import sys

#def main() -> None:

#    input = sys.stdin.readline
#    word = input().strip()
#    values = [0 for i in range(26)]
    
#    alphabet_index = {chr(ord("A") + i) : i for i in range(26)}

#    for i in word.upper():
#        values[alphabet_index[i]] += 1

#    sys.stdout.write(" ".join(map(str, values)))

import sys

word = sys.stdin.readline().strip()
values = [0]*26

for ch in word.upper():           # 대문자 통일
    idx = ord(ch) - 65            # 'A'의 ASCII 코드 65
    if 0 <= idx < 26:             # 안전: 알파벳만
        values[idx] += 1

print(' '.join(map(str, values)))

    
        