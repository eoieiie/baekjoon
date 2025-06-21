import sys

def main() -> None:

  input = sys.stdin.readline
  n = int(input())
  output = []
  stack = []
  temp = 1
  isitok = True

  for _ in range(n):
    
    num = int(input())
    
    while temp <= num:
      stack.append(temp)
      output.append("+")
      temp += 1

    if stack and stack[-1] == num:
      stack.pop()
      output.append("-")

    else:
      isitok = False
      break

  if isitok:
    
    sys.stdout.write("\n".join(output))
  else:
    sys.stdout.write("NO")
    
if __name__ == "__main__":
  main()

  