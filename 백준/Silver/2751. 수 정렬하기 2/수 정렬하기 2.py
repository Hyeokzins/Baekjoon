import sys

N = int(sys.stdin.readline().rstrip())
num_list = []

for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)

num_list = sorted(set(num_list))

for num in num_list:
    print(num)