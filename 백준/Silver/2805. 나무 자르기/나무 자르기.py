import sys

N,M=map(int,sys.stdin.readline().rstrip().split())

A=[int(x) for x in sys.stdin.readline().rstrip().split()]
A.sort()

def test(A, H):
    k = sum(max(i - H, 0) for i in A)
    return k >= M

def Parametric_search(lo, hi):
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if test(A,mid):
            lo = mid  
        else:
            hi = mid

    print(lo)

Parametric_search(0,max(A))

