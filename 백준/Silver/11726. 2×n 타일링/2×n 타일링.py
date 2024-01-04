n = int(input())

a=1
b=2
c=0


if n==1:
    c=1
    
elif n==2:
    c=2


elif n>=3:
    for i in range(n-2):
        c=b+a
        a=b
        b=c
    

print(c%10007)