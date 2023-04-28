N,M=map(int,input().split())

a=list(range(1,N+1))

for z in range(M):
    i,j,k=map(int,input().split())
    i=i-1
    j=j-1
    k=k-1

    part=a[i:j+1]
    change=part[-(j-k+1):]+part[:-(j-k+1)]

    finals=a[:i]+change+a[j+1:]
   
    ##a[i:k],a[k:j+1]=a[k:j+1],a[i:k]
    a=finals




print(*a)