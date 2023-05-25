import sys
import math
from collections import Counter
N = int(sys.stdin.readline())

num_list=[]
for i in range(N):
    a = int(sys.stdin.readline())
    num_list.append(a)

avg=round(sum(num_list)/N)
print(avg)

num_list.sort()

mid=num_list[(len(num_list)//2)]
print(mid)

num_count_list=Counter(num_list)

value=list(num_count_list.values())
if value.count(max(value))>1:
    print(num_count_list.most_common()[1][0])
else:
    print(num_count_list.most_common()[0][0])

print(abs(num_list[-1]-num_list[0]))
