import sys
input = sys.stdin.readline

n = int(input().strip())
company = []
for _ in range(n) :
    name, log = input().split()
    if log == 'enter' :
        company.append(name)
    else :
        if name in company :
            company.pop(company.index(name))

company.sort(reverse=True)
for member in company :
    print(member)