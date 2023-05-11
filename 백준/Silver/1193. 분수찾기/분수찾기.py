import sys 
X = int(sys.stdin.readline())
a,b=1,1
Direction=1 # 방향 지정 수 생성

if X>1:
    for i in range(X-1):
        if Direction==1:
            a=a-1
            b=b+1
            if a==0:
                a+=1
                Direction=0
        else:
            a=a+1
            b=b-1
            if b==0:
                b+=1
                Direction=1

print("{}/{}".format(a, b))