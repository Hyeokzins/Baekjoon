import sys
N=int(sys.stdin.readline().rstrip())

b=N//5

if N%5==0:
    print(b)
elif N%5==1:
    print((N//5)+1)
elif N%5==2:
    if b==1:
        print('-1')
    else:
        print((N//5)+2)
elif N%5==3:
    print(b+1)
elif N%5==4:
    if b==0:
        print(-1)
        
    else:
        print((N//5)+2)
