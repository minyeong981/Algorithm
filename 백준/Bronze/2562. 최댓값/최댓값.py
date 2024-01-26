max = 0

for num in range(9) :
    number = int(input())
    if number > max :
        max = number
        if max == number :
            idx = num +1 

print(max)
print(idx)