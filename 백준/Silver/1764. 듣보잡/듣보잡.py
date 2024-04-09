N, M = map(int, input().split())
notHear = set()
for _ in range(N):
    notHear.add(input())

notSee = set()
for _ in range(M):
    notSee.add(input())

notHS = set.intersection(notHear, notSee)

print(len(notHS))
for result in sorted(notHS) :
    print(result)

