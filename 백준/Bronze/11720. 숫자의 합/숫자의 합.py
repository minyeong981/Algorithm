N = int(input())
num = int(input())
num_lst = []

for i in str(num) :
    num_lst.append(i) #문자열로 분리

# while (num != 0) :
#     num_lst.append(num%10)
#     num= num//10 # 숫자형으로 분리

sum_V = 0
for ele in num_lst :
    sum_V = sum_V + int(ele)
print(sum_V)