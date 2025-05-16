from collections import defaultdict

# 두 좌표 사이의 이동 경로를 생성하는 함수
# 상하(r 좌표)를 먼저 이동하고, 좌우(c 좌표)를 나중에 이동
def getSteps(startPos, endPos):
    sr, sc = startPos
    er, ec = endPos
    path = []

    r, c = sr, sc
    while r != er:
        r += 1 if r < er else -1
        path.append((r, c))  # r 좌표 이동
    while c != ec:
        c += 1 if c < ec else -1
        path.append((r, c))  # c 좌표 이동

    return path

def solution(points, routes):
    # timePositionCount[time][(r, c)] = 해당 시간에 해당 위치에 있는 로봇 수
    timePositionCount = defaultdict(lambda: defaultdict(int))

    # 각 로봇별로 이동 경로를 시뮬레이션
    for route in routes:
        time = 0
        # 출발 위치 (0초에 위치함)
        currentPos = points[route[0] - 1]
        timePositionCount[time][tuple(currentPos)] += 1

        # 각 구간별 이동 처리
        for i in range(1, len(route)):
            nextPos = points[route[i] - 1]
            steps = getSteps(currentPos, nextPos)

            for pos in steps:
                time += 1  # 1초에 한 칸 이동
                timePositionCount[time][pos] += 1

            currentPos = nextPos  # 다음 이동 시작점 갱신

    # 위험 상황 계산: 같은 시간에 같은 좌표에 2대 이상 있으면 위험 1회
    dangerCount = 0
    for time in timePositionCount:
        for count in timePositionCount[time].values():
            if count >= 2:
                dangerCount += 1

    return dangerCount
