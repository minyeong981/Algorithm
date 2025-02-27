import sys
input = sys.stdin.readline

N = map(int, input().strip())
cards = list(map(int, input().split()))
M = map(int, input().strip())
sg = list(map(int, input().split()))
dic = {}
for card in cards :
    dic[card] = 1
for sgCard in sg :
    print(dic.get(sgCard, 0), end=' ')