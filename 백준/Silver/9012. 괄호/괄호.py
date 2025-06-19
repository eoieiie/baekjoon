import sys

out_lines = []
def main():
    
    input = sys.stdin.readline
    n = int(input())
    
    for _ in range(n):
        
        stack = []
        ps = input().rstrip()
        
        for i in ps:
            if i == "(":
                stack.append(i)
                
            elif i == ")" and stack:
                stack.pop()

            elif i == ")" and not stack:
                stack.append(")")
                break
    
        out_lines.append("NO" if stack else "YES")
            
    sys.stdout.write('\n'.join(out_lines))

if __name__ == "__main__":
    main()
