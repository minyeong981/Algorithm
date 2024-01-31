lst = []
for num in range(10):
    A = int(input())
    lst.append(A%42)
    result = set(lst)
print(len(result))