from collections import deque
import sys

input = sys.stdin.readline

def main() -> None:

  output = [] # 함수의 전역 변경을 최소화, 테스트와 재사용을 용이하게 함. 
  que = deque()

  
  n = int(input())

  for _ in range(n):
    command, *args = input().split()
  
    if command == "push_front":
      que.appendleft(args[0])
      
    elif command == "push_back":
      que.append(args[0])
  
    elif command == "pop_front":
      if not que:
        output.append("-1")
      else:
        output.append(que.popleft())
      
    elif command == "pop_back":
      if not que:
        output.append("-1")
      else:
        output.append(que.pop())
      
    elif command == "size":
      output.append(str(len(que)))
      
    elif command == "empty":
      if not que:
        output.append("1")
      else:
        output.append("0")
        
    elif command == "front":
      if not que:
        output.append("-1")
      else:
        output.append(que[0])
    elif command == "back":
      if not que:
        output.append("-1")
      else:
        output.append(que[-1])
  
  sys.stdout.write("\n".join(output))

if __name__ == "__main__":
  main()

#또는!
  
# # deque_refactored_final.py
# from collections import deque
# import sys
# from typing import Deque, List, Callable, Dict   # ── 타입 힌트용 ──

# def main() -> None:
#     input = sys.stdin.readline
#     n: int = int(input())                        # 명령 개수

#     dq: Deque[str] = deque()                     # 덱
#     out: List[str] = []                          # 출력 버퍼

#     # ────────────────────── push 계열 ──────────────────────
#     #  push 명령은 항상 "값 1개"를 인자로 받으므로
#     #  deque의 메서드 포인터를 그대로 매핑해 재사용.
#     push_ops: Dict[str, Callable[[str], None]] = {
#         "push_front": dq.appendleft,
#         "push_back":  dq.append,
#     }

#     # ───────────────────── 나머지 연산 ─────────────────────
#     #  빈 덱 검사 → 결과 out에 추가 → 리턴값 None
#     def pop_front() -> None:
#         out.append(dq.popleft() if dq else "-1")

#     def pop_back() -> None:
#         out.append(dq.pop() if dq else "-1")

#     def size() -> None:
#         out.append(str(len(dq)))

#     def empty() -> None:
#         out.append("0" if dq else "1")

#     def front() -> None:
#         out.append(dq[0] if dq else "-1")

#     def back() -> None:
#         out.append(dq[-1] if dq else "-1")

#     other_ops: Dict[str, Callable[[], None]] = {
#         "pop_front": pop_front,
#         "pop_back":  pop_back,
#         "size":      size,
#         "empty":     empty,
#         "front":     front,
#         "back":      back,
#     }

#     # ────────────────────── 명령 루프 ──────────────────────
#     for _ in range(n):
#         cmd, *arg = input().split()

#         if cmd in push_ops:          # push X —> 인자 필수
#             push_ops[cmd](arg[0])
#         else:                        # 나머지 —> 미리 만들어둔 함수 실행
#             other_ops[cmd]()

#     sys.stdout.write("\n".join(out))

# if __name__ == "__main__":
#     main()