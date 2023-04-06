from itertools import zip_longest

word_num=0
matrix_1=[]
while word_num<5:
    x=input()
    if x.isalnum() and len(x)>= 1 and  len(x)<=15:
        matrix_1.append(x)
        word_num += 1
"""
max_word=0

for i in range(len(matrix_1)):
    if len(matrix_1[i])>max_word:
        max_word=len(matrix_1[i])

print('max_word:',max_word)

matrix_2=[]

for j in range(max_word):
    try:
        for i in range(len(matrix_1)):
            matrix_2.append(matrix_1[i][j])
    except IndexError:
        for i in range(len(matrix_1)):
            matrix_2.append(matrix_1[i+1][j])

"""
matrix_2=[a for a in zip_longest(*matrix_1)]

result = ''
for i in matrix_2:
    for j in i:
        if j is not None:
            result += j

print(result)