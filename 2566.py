matrix_1=[[x for x in map(int,input().split())] for i in range(9)]
max=0
max_i=0
max_j=0


for i in range(9):
    for j in range(9):
        if matrix_1[i][j]>=max:
            max=matrix_1[i][j]
            max_i=i
            max_j=j


print(matrix_1[max_i][max_j])

print(max_i+1,max_j+1)
