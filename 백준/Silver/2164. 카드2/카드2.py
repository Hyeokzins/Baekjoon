import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
card=deque()

for i in range(1,N+1):
    card.appendleft(i)


while len(card)>1:
    card.pop()
    card.rotate(1)

print(card[0])
    


