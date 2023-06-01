import sys
N = int(sys.stdin.readline().rstrip())

k=[]
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    k.append(num)


test=[]
command=[]
test.append(1)

command.append('+')

i=2
while i<N+2:
    if len(test)>0:
        if test[-1]==k[0]:
            test.pop()
            
            command.append('-')
            k.pop(0)
        else:
            if i<N+1:
                test.append(i)
                
                command.append('+')
                i+=1
            else:
                break
    else:
        if i<N+1:
            test.append(i)
            
            command.append('+')
            i+=1
        else:
            break

if len(test)>0:
    print('NO')
else:
    for i in range(len(command)):
        print(command[i])



         

    
    
