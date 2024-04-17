from collections import deque

def solution(graph, start):
    visited = list() #방문한 노드를 저장하는 리스트 
    queue = deque() # bfs를 위한 큐
    
    queue.append((start,0))
    visited.append(start)
    howlen=list() #각 노드까지의 거리를 저장하는 리스트
    while queue:
        node, count = queue.popleft()
        if node in graph:
            for i in graph[node]:
                if i not in visited:
                    visited.append(i)
                    howlen.append((i,count+1))
                    queue.append((i,count+1))
    howlen.sort(key = lambda x : (-x[1],-x[0]))
    return howlen[0][0]

for test_case in range(1,11): #10번 반복할건데 
    N, start = map(int,input().split()) #일단 노드의 개수와 시작 노드를 입력받는다. 
    numlist = list(map(int,input().split())) #간선 정보를 입력받는다. 
    graph={} #그래프를 나타내는 딕셔너리. 예) {1: [2, 3], 2: [1, 4], ...}
    for i in range(0,N,2): #입력된 간선 정보를 그래프로 변환하는 작업...
        if numlist[i] not in graph:
            graph[numlist[i]] = [numlist[i+1]]
        else:
            graph[numlist[i]].append(numlist[i+1])

    print('#{} {}'.format(test_case, solution(graph,start)))



#쉽게 말하자면 주어진 그래프와 시작 노드를 받아서 함수를 수행하고, 가장 멀리 떨어진 노드를 찾아서 반환하는 문제.
# 여기서 dfs인지 bfs인지 판별하는 방법은, 큐를 사용하냐 안 하냐, 팝을 이용하요 큐에서 값을 빼고 넣느냐의 관점엣서 보면 된다. 
