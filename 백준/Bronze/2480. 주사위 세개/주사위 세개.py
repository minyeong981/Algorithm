fir, sec, thir = map(int, input().split())
if fir == sec == thir :
    print(10000 + fir*1000)
elif fir == sec or fir == thir :
    print(1000 + fir*100)
elif sec == thir :
    print(1000 + thir*100)
else :
    print(max(fir, sec, thir)*100)