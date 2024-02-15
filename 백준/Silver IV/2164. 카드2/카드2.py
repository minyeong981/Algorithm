from collections import deque
N = int(input())
cards = deque()
for card in range(1,N+1) :
    cards.append(card)
while len(cards)>1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)