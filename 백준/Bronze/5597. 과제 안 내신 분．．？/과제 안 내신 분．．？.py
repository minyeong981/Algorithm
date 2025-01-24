lst = set(range(1, 31))  # 1부터 30까지의 숫자

for _ in range(28):
    num = int(input())  # 출석한 학생 번호
    lst.remove(num)  # 출석한 학생을 리스트에서 제거

# 남아있는 학생을 출력
for student in sorted(lst):
    print(student)