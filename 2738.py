N,M=map(int,input().split())

matrix_1=[[x for x in map(int,input().split())] for i in range(N)]
matrix_2=[[x for x in map(int,input().split())] for i in range(N)]

result = [[sum(row) for row in zip(*i)]for i in zip(matrix_1,matrix_2)]

for i in range(len(result)):
    print(*result[i])

