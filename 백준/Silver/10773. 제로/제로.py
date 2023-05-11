import sys
N= int(sys.stdin.readline())

money=[]
for i in range(N):
    a= int(sys.stdin.readline())
    if a==0:
        try:
            money.pop()
        except IndexError:
            money.append(0)
    
    else:
        money.append(a)

print(sum(money))
