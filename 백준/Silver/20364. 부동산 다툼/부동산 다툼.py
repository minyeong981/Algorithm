import sys
input = sys.stdin.readline

N,Q = map(int, input().split())

visited = [0] * (N+1)

for _ in range(Q) :
    k = int(input())
    goal = k
    flag = 0 # 다른 오리의 점유된 땅 번호

    while goal != 1 :
        if visited[goal] > 0 : # 이미 땅이 점유되었다면
            flag = goal
        goal //= 2 # 목표지까지 이동

    if flag :
        print(flag)
    else : # 원하는 땅까지 점유된 곳이 없었다면
        visited[k] = 1 # 방문 표시
        print(0)
