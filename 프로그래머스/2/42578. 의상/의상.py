from collections import defaultdict

def solution(clothes):
    clothes_dic = defaultdict(list)

    # 종류별로 의상 이름 저장
    for name, kind in clothes:
        clothes_dic[kind].append(name)
    
    # 조합 수 계산
    answer = 1
    for kind in clothes_dic:
        answer *= (len(clothes_dic[kind]) + 1)  # 안 입는 경우 포함
    
    return answer - 1  # 아무것도 안 입는 경우 제외
