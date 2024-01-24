A, B, C = map(int, input().split())
D = int(input())

sec = (C+D)%60
minute_ = (C+D)//60

if minute_+B < 60 :
    minute = minute_+B
    hour = A
    print(hour, minute, sec)
else :
    minute = (minute_+B)%60
    hour = A+(minute_+B)//60
    if hour > 23 :
        hour = hour%24
        print(hour, minute, sec)
    else :
        print(hour, minute, sec)