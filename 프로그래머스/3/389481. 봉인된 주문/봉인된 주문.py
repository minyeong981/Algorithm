def get_index(s):
    idx = 0
    for l in range(1, len(s)):
        idx += 26 ** l
    for i in range(len(s)):
        idx += (ord(s[i]) - ord('a')) * (26 ** (len(s) - i - 1))
    return idx + 1

def get_string_from_index(index):
    total = 0
    for length in range(1, 12):
        count = 26 ** length
        if total + count >= index:
            offset = index - total - 1
            s = ""
            for _ in range(length):
                s = chr(ord('a') + offset % 26) + s
                offset //= 26
            return s
        total += count
    return ""

def solution(n, bans):
    # 1. 삭제된 문자열들의 사전 순 인덱스를 계산
    banned_indices = sorted(get_index(b) for b in bans)

    # 2. 이진 탐색
    left, right = 1, 10**16
    answer_idx = -1

    def count_banned_leq(x):
        # x보다 작거나 같은 삭제 인덱스 개수
        lo, hi = 0, len(banned_indices)
        while lo < hi:
            mid = (lo + hi) // 2
            if banned_indices[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    while left <= right:
        mid = (left + right) // 2
        banned_before = count_banned_leq(mid)
        valid_count = mid - banned_before
        if valid_count >= n:
            answer_idx = mid
            right = mid - 1
        else:
            left = mid + 1

    return get_string_from_index(answer_idx)
