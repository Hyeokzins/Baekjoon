a=input().split(' ')
k=len(a)

if a[0]=='':
    k-=1
    if a[-1]=='':
        k-=1
elif a[-1]=='':
    k-=1
    if a[0]=='':
        k-=1

print(k)

