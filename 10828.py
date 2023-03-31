
command_num=int(input())  #명령내릴 횟수를 입력받아 저장

stack=[]

def stack_process (command):
    if command.count(' ')==1: #명령에 공백이 있다면 앞(명령 종류)뒤(변수)로 분리
        command_type,command_variable=command.split()
        command_variable=int(command_variable)
        stack.append(command_variable)
    else:
        command_type=command
        if command_type=='pop':
            if len(stack)==0:
                print(-1)

            else:
                print(stack.pop())
        elif command_type=='size':
            print(len(stack))
        elif command_type=='empty':
            if len(stack)==0:
                print(1)
            else:
                print(0)
        elif command_type=='top':
            if len(stack)==0:
                print(-1)
            else:
                print(stack[-1])

command_list=[]

for i in range(command_num):    #명령내릴 횟수만큼 반복
    command=input()
    command_list.append(command)
    

for j in range(command_num):
    (stack_process(command_list[j])) 
    
    
    
   

