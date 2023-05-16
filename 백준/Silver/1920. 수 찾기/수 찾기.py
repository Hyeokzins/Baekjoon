import sys
N=int(sys.stdin.readline().rstrip())
A=[x for x in map(int,list(sys.stdin.readline().rstrip().split()))]
A.sort()

M=int(sys.stdin.readline().rstrip())
B=[x for x in map(int,list(sys.stdin.readline().rstrip().split()))]
B_sort=sorted(B)
       
def detect(i):
    target=B[i]
    left=0
    right=N-1
    answer=0

    while left<=right:
        mid=(left+right)//2
        if A[mid]==target:
            answer=1
            break
        elif A[mid]>target:
            right=mid-1
        else:
            left=mid+1
    print(answer)

for i in range(M):
    detect(i)