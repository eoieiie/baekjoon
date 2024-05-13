def getsome(here,hour):
    for next in mymap[here]:
        if distance[next]>=hour + 1:
            distance[next] = hour + 1
            getsome(next, hour + 1)


for tc in range(1, 11):
    ans = 0
    max_distance = 0
    howmany, start = map(int, input().split())
    data = list(map(int, input().split()))

    distance = [9999] * 101
    mymap = [[]for _ in range(101)]

    for i in range(0, len(data), 2):
        _from, _to = data[i], data[i + 1]
        mymap[_from].append(_to)  

    getsome(start, 0)

    for i in range(1, len(distance)):
        if distance[i] >=max_distance and distance[i] != 9999:
            max_distance = distance[i]
            ans = i

    print("#%d %d" %(tc,ans))