def binary_search(arr, target):
    #우선 시작과 끝 지점을 설정한다. 일반적으로 시작 지점은 0, 끝 지점은 배열의 길이 -1이다. 
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

N = int(input())
A = list(map(int, input().split()))
A.sort()  # 리스트 A를 정렬해야 이분 검색을 할 수 있음

M = int(input())
B = list(map(int, input().split()))

for i in B:
    if binary_search(A, i):
        print(1)
    else:
        print(0)
