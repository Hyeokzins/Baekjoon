import sys
while True:
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    A.sort()
    if A[0]==A[1]==A[2]==0:
        break
    if A[2]**2==A[0]**2+A[1]**2:
        print('right')
    else:
        print('wrong')
    