N = int(input()) # 과목 개수
scores = list(map(int, input().split())) # 현재 성적
M = max(scores) # 최댓값
new_score = []
sum_score = 0

for score in scores :
    new_score.append(score/M*100)

for add in new_score :
    sum_score += add
print(sum_score/N)
