import sys

N,M=map(int,sys.stdin.readline().rstrip().split())

non_listen_list={tuple(sys.stdin.readline().rstrip().split()) for _ in range(N)}
non_see_list={tuple(sys.stdin.readline().rstrip().split()) for _ in range(M)}

non_listen_see=non_listen_list&non_see_list

sorted_set = sorted(non_listen_see)
print(len(sorted_set)) 

for i in sorted_set:
    print(*i)
