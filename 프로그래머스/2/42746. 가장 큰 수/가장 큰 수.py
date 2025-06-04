from functools import cmp_to_key

def compare(x, y):
    # 두 숫자를 문자열로 이어붙여 큰 쪽이 앞에 오도록
    if x + y > y + x:
        return -1  # x가 먼저
    elif x + y < y + x:
        return 1   # y가 먼저
    else:
        return 0

def solution(numbers):
    # 숫자들을 문자열로 바꿔서 비교
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    result = ''.join(numbers)
    # 예외 처리: 모두 0일 경우 "000" -> "0"
    return result if result[0] != '0' else '0'
