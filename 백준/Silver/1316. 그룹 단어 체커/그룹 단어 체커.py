import sys
N= int(sys.stdin.readline())
not_group=0
new_not_group=0
for i in range(N):
    a=input()
    
    for i in range(len(a)-2):
        for j in range(i+2,len(a)):
            if a[i]==a[j]:
                if a[i]==a[i+1]:
                    continue
                new_not_group=not_group+1
                break
        if new_not_group!=not_group:
            break
    not_group=new_not_group

print(N-not_group)


            