def solution(friends, gifts):
    n = len(friends)
    name_to_index = {name: i for i, name in enumerate(friends)}
    
    # 선물 기록: give[i][j] = i가 j에게 준 선물 수
    give = [[0] * n for _ in range(n)]
    for g in gifts:
        a, b = g.split()
        give[name_to_index[a]][name_to_index[b]] += 1

    # 선물 지수 계산
    gift_score = [0] * n
    for i in range(n):
        gift_score[i] = sum(give[i]) - sum(give[j][i] for j in range(n))

    # 다음달 받을 선물 수
    next_received = [0] * n

    # 중복 없이 (i < j) 쌍만 비교
    for i in range(n):
        for j in range(i + 1, n):
            give_i_j = give[i][j]
            give_j_i = give[j][i]

            if give_i_j > give_j_i:
                next_received[i] += 1
            elif give_i_j < give_j_i:
                next_received[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    next_received[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_received[j] += 1
                # 같으면 아무 일 없음

    return max(next_received)
