from collections import defaultdict

def dfs(airport) :
    while graph[airport]:
        nextAirport = graph[airport].pop()
        dfs(nextAirport)
    path.append(airport)  # 마지막 공항부터 거꾸로 쌓임
    
def solution(tickets):
    global graph, path
    
    graph = defaultdict(list)

    # 출발지를 키로, 도착지를 리스트로 모으고 정렬
    for start, end in tickets:
        graph[start].append(end)

    # 사전 순으로 방문해야 하므로 각 리스트를 정렬
    for key in graph:
        graph[key].sort(reverse=True)  # 나중에 pop() 쓰려고 reverse 정렬

    path = []
    dfs("ICN")

    return path[::-1]  # 뒤집어서 정답 리턴