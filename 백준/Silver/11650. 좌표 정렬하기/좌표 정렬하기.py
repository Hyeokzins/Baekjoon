import sys
N = (int(sys.stdin.readline().rstrip()))
num_list=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

num_list.sort()

for i in num_list:
    for particle in i:
        print(particle, end=' ')
    print()