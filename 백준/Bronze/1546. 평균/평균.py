N=int(input())

grade=[x for x in map(int,input().split())]

sum=0

for i in range(N):
    sum+=grade[i]/max(grade)*100
    
print(sum/N)
