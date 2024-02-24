N = int(input())
switches = [-1] + list(map(int, input().split()))
students = int(input())

def male(switches, s_no) :
    for idx in range(s_no, N+1, s_no) :
        switches[idx] = 1 - switches[idx]

def female(switches, s_no) :
    left = s_no -1
    right = s_no +1
    switches[s_no] = 1 - switches[s_no]
    while 0 < left and N >= right and switches[left] == switches[right] :
        switches[left] = 1 - switches[left]
        switches[right] = 1 - switches[right]
        left -= 1
        right += 1

for _ in range(students) :
    sex, s_no = map(int, input().split())
    if sex == 1 :
        male(switches, s_no)
    else :
        female(switches, s_no)

if N <= 20 :
    print(*switches[1:])
else:
    for i in range(1, N + 1, 20):
        end_idx = min(i + 20, N + 1)  # 인덱스 범위 설정
        print(*switches[i:end_idx])