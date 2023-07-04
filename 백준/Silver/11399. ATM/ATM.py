import sys
N = (int(sys.stdin.readline().rstrip()))

num_list=list(map(int,sys.stdin.readline().rstrip().split()))

num_list.sort()
total=0
sum_list=[]
for i in num_list:
    total+=i
    sum_list.append(total)

print(sum(sum_list))
