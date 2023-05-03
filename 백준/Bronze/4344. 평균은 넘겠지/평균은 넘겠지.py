C=int(input())
avg_list=[]

for i in range(C):
    test=[x for x in map(int,input().split())]
    sum=0
    for j in range(1,len(test)):
        sum=test[j]+sum
    avg=(sum/test[0])

    test_upper=[test[i] for i in range(1,len(test)) if test[i]>avg]
    per=((len(test_upper)/(len(test)-1))*100)
    avg_list.append(per)

for i in range(C):
    print("{:.3f}%".format(avg_list[i]))
