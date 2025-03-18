import sys
input = sys.stdin.readline

def solve(arr, target) :
    s, e = 0, len(arr) - 1
    while s <= e :
        mid = (s + e) // 2

        if arr[mid] == target :
            return mid

        if arr[mid] > target :
            e = mid - 1
        else :
            s = mid + 1

    return s

N = int(input().rstrip())
A = list(map(int, input().split()))
lst = []
for num in A :
    if len(lst) == 0 or lst[-1] < num :
        lst.append(num)
    else :
        lst[solve(lst, num)] = num

print(len(lst))