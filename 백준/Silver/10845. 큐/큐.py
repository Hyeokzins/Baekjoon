import sys
command_num=int(sys.stdin.readline().rstrip())  #명령내릴 횟수를 입력받아 저장

que=[]

def que_process (command):
    if command.count(' ')==1: #명령에 공백이 있다면 앞(명령 종류)뒤(변수)로 분리
        command_type,command_variable=command.split()
        command_variable=int(command_variable)
        que.append(command_variable)
    else:
        command_type=command
        if command_type=='pop':
            if len(que)==0:
                print(-1)

            else:
                print(que.pop(0))
        elif command_type=='size':
            print(len(que))
        elif command_type=='empty':
            if len(que)==0:
                print(1)
            else:
                print(0)
        elif command_type=='front':
            if len(que)==0:
                print(-1)
            else:
                print(que[0])
        elif command_type=='back':
            if len(que)==0:
                print(-1)
            else:
                print(que[-1])

for i in range(command_num):    #명령내릴 횟수만큼 반복
    command=(sys.stdin.readline().rstrip())
    que_process(command)
    


    