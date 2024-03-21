def combi(k, s):
    global minV

    if k == teamNum:  # 팀이 나눠진 경우
        start_team = []  # 스타트 팀
        link_team = []  # 링크 팀
        for i in range(N):
            if visited[i]:  # 방문한 경우 스타트 팀
                start_team.append(i)
            else:  # 아닌 경우 링크 팀
                link_team.append(i)

        # 각 팀의 능력치 계산
        start_ability = 0
        link_ability = 0
        for i in range(teamNum):
            for j in range(i + 1, teamNum):  # 중복을 피하기 위해 i+1부터 시작
                start_ability += arr[start_team[i]][start_team[j]] + arr[start_team[j]][start_team[i]]
                link_ability += arr[link_team[i]][link_team[j]] + arr[link_team[j]][link_team[i]]
        result = abs(start_ability - link_ability)

        # 최소값 갱신
        minV = min(minV, result)
        return

    # 조합 생성
    for i in range(s, N - teamNum + k + 1):  # 팀의 능력을 중복되지 않도록 설정
        visited[i] = True
        combi(k + 1, i + 1)
        visited[i] = False


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
teamNum = N // 2
visited = [False] * N
minV = float('inf')
combi(0, 0)
print(minV)
