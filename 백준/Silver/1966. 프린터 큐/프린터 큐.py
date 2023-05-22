import sys
from collections import deque
x=int(sys.stdin.readline())
for i in range(x):
    N,M=map(int,sys.stdin.readline().rstrip().split())
    A=list(map(int, sys.stdin.readline().rstrip().split()))
    TEST=deque()
    for i in A:
        TEST.appendleft(i)
        key_value=[i for i in range(len(TEST))]
        key=deque()
    for i in key_value:
        key.appendleft(i)
    num=0
    key1=key[-(M+1)]
    while (key1 in key):
        if TEST[-1]>= max(TEST):
            TEST.pop()
            key.pop()
            num+=1
        else:
            TEST.rotate(1)
            key.rotate(1)

    print(num)
 