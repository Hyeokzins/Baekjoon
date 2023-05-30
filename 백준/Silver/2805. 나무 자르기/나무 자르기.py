import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))


def test(A, H):
    k = 0
    for i in A:
        if i > H:
            k += i - H
    return k >= M


def Parametric_search(lo, hi, A):
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if test(A, mid):
            lo = mid
        else:
            hi = mid

    print(lo)


Parametric_search(0, max(A), A)