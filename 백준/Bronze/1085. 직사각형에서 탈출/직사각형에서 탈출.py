import sys
A = list(map(int, sys.stdin.readline().rstrip().split()))

A[2]-=A[0]
A[3]-=A[1]

print(min(A))


