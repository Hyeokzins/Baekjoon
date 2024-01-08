import sys
N = (int(sys.stdin.readline().rstrip()))
num_list=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

sorted_list = sorted(num_list, key=lambda x: (x[1], x[0]))


seminar_list=[]

seminar_list.append(sorted_list[0])

#판단기준
x=sorted_list[0][1]

#print(seminar_list)
#print(x)


for i in sorted_list[1:]:
    if x<=i[0]:
        #print('이번 턴은',i)
        seminar_list.append(i)
        x=i[1]
        #print('x로 변경된값은?',x)
#print(seminar_list)

print(len(seminar_list))