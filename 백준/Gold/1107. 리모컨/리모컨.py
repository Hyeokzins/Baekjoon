import sys

X=(int(sys.stdin.readline().rstrip()))

N = (int(sys.stdin.readline().rstrip()))

if N==0:
    num_list=[]
else:
    num_list=list(map(int,sys.stdin.readline().rstrip().split()))

# print(X)
# print(N)
# print(num_list)

base= int(100) #시작 채널

dsa=abs(X-base) #시작 채널에서 목표채널로 +-버튼으로 갈수있는 경우의수 

available_num = [i for i in range(10) if i not in num_list] #사용가능한 번호 리스트

#print(available_num)
station=[]
station_flag1=[]
station_flag2=[]
station_up=[]
station_up2=[]
station_down=[]
station_reverse=[]
station_reverse2=[]
str_number=str(X)
up_number = int(str(int(str_number[0]) + 1) + str_number[1:])
down_number = int(str(int(str_number[0]) - 1) + str_number[1:])

#일반적인 상태를 0으로 정함
flag=0

if N!=10: #버튼 10개 고장난 사례가 아니라면
    for u,i in enumerate(str(X)):
        if flag==0: #일반적인 상황일때
            #print('현재탐색 숫자는',i)
            #현재 자리수와 절대값이 가까운 숫자를 찾는다
            closest_numbers = [num for num in available_num if abs(num - int(i)) == min(abs(n - int(i)) for n in available_num)]
            #print(closest_numbers)
            if len(closest_numbers)==1: #만약 가까운숫자가 1개라면
                station.append(closest_numbers[0]) #더한다
                ##print(closest_numbers[0],'를 더했습니다')
                if closest_numbers[0]<int(i):
                    flag=1
                    station_flag1=station.copy()
                elif closest_numbers[0]>int(i):
                    station_flag2=station.copy()
                    flag=2

            else: #만약 가까운숫자가 2개라면 작은숫자와 큰숫자 둘다 진행해보아야함
                #print(closest_numbers,'이므로 분기점 세우겠습니다')

                for p in range(len(closest_numbers)):
                    if p==0:
                        station_flag1=station.copy()
                        station_flag1.append(closest_numbers[0])
                        #print('플래그1에 ',closest_numbers[0],'더했습니다')
                        
                        for k in range(len(str(X))-(u+1)):
                            closest_number = min(available_num, key=lambda a: abs(a - 9))
                            station_flag1.append(closest_number)

                        

                    elif p==1:
                        station_flag2=station.copy()
                        station_flag2.append(closest_numbers[1])
                        #print('플래그2에 ',closest_numbers[1],'더했습니다')

                        for k in range(len(str(X))-(u+1)):
                            #print('플래그2 시작')
                            #print(len(str(X))-(u+1))
                            closest_number = min(available_num, key=lambda a: abs(a - 0))
                            station_flag2.append(closest_number)
                            #print('플래그2에 ',closest_number,'더했습니다')
                break            

        elif flag==1:
            
            closest_number = min(available_num, key=lambda a: abs(a - 9))
            station_flag1.append(closest_number)

        elif flag==2:
            
            closest_number = min(available_num, key=lambda a: abs(a - 0))
            station_flag2.append(closest_number)


    if X!=0:
        if len(station)>1:
            if station[0]==0:
                del station[0]

    for num ,c in enumerate(str(X)[::-1]):
        if num==0:
            closest_number_reverse = min(available_num, key=lambda a: abs(a - 0))
            station_reverse.append(closest_number_reverse)

        else:
            if (int(c)+1)==10:
                closest_number_reverse = min(available_num, key=lambda a: abs(a - 0))
                station_reverse.append(closest_number_reverse)
            else:
                closest_number_reverse = min(available_num, key=lambda a: abs(a - (int(c)+1)))
                station_reverse.append(closest_number_reverse)

    flag2=0
    for num ,c in enumerate(str(X)[::-1]):

        if flag2==0:
            #print('플래그2=0')
            if int(c)==0:
                vs=10
            else:
                vs=int(c)
        
            closest_number_reverse2 = min(available_num, key=lambda a: abs(a - vs))
            station_reverse2.append(closest_number_reverse2)
            #print(station_reverse2)
            if int(c)< vs:
                flag2=1
            else:
                flage2=0
        else:
            #print('플래그2=1')
            
            if int(c)==0:
                vs=9
            else:
                vs=int(c)-1
        
            closest_number_reverse2 = min(available_num, key=lambda a: abs(a - vs))
            station_reverse2.append(closest_number_reverse2)
            #print(station_reverse2)

            if int(c)< vs:
                
                flag2=1
            else:
                #print(int(c),vs)
                flag2=0

    station_reverse.reverse()
    station_reverse2.reverse()
    #print(station_reverse)      


    if 1 in available_num:
        station_up2=[1]          
        for q in range(len(str(X))):
            closest_number_up2 = min(available_num, key=lambda a: abs(a - 0))
            station_up2.append(closest_number_up2)

        

    #한자리 더 큰수 에서 탐색
    for idx, j in enumerate(str(up_number)):

        if idx==0:
            closest_number_up = min(available_num, key=lambda a: abs(a - int(j)))
            station_up.append(closest_number_up)
        else:
            closest_number_up = min(available_num, key=lambda a: abs(a - 0))
            station_up.append(closest_number_up)

    if down_number>=0:
        for idx, j in enumerate(str(down_number)):
            if idx==0:
                closest_number_down = min(available_num, key=lambda a: abs(a - int(j)))
                station_down.append(closest_number_down)
            else:
                closest_number_down = min(available_num, key=lambda a: abs(a - 9))
                station_down.append(closest_number_down)

    if len(str(X))>1:
        station_down2=[]
        for u in range(len(str(X))-1):
            closest_number_down2 = min(available_num, key=lambda a: abs(a - 9))
            station_down2.append(closest_number_down2)
    
    if len(station)>0:
        station_num=int(''.join(map(str, station)))
        #print('station_num:',station_num)
        walk=abs(X-station_num)
        result=(len(station)+walk)
    
    if len(station_flag1)>0:
        station_flag1_num=int(''.join(map(str, station_flag1)))
        #print('station_flag1_num',station_flag1_num)
        walk_flag1=abs(X-station_flag1_num)
        result_flag1=(len(station_flag1)+walk_flag1)

    if len(station_flag2)>0:    
        station_flag2_num=int(''.join(map(str, station_flag2)))
        #print('station_flag2_num',station_flag2_num)
        walk_flag2=abs(X-station_flag2_num)
        result_flag2=(len(station_flag2)+walk_flag2)

    if len(station_up)>0:

        station_up_num=int(''.join(map(str, station_up)))
        #print('station_up_num:',station_up_num)
        walk_up=abs(X-station_up_num)
        result_up=(len(station_up)+walk_up)
    if len(station_up2)>0:
        station_up2_num=int(''.join(map(str, station_up2)))
        #print('station_up2_num:',station_up2_num)
        walk_up2=abs(X-station_up2_num)
        result_up2=(len(station_up2)+walk_up2)

    
    if len(station_down)>0:
        station_down_num=int(''.join(map(str, station_down)))
        walk_down=abs(X-station_down_num)
        result_down=(len(station_down)+walk_down)
    
    if len(station_reverse)>0:

        station_reverse_num=int(''.join(map(str, station_reverse)))
        #print('station_reverse_num:',station_reverse)
        walk_reverse=abs(X-station_reverse_num)
        result_reverse=(len(station_reverse)+walk_reverse)

    if len(station_reverse2)>0:

        station_reverse2_num=int(''.join(map(str, station_reverse2)))
        #print('station_reverse2_num:',station_reverse2)
        walk_reverse2=abs(X-station_reverse2_num)
        result_reverse2=(len(station_reverse2)+walk_reverse2)


    if 'station_down2' in locals():
        station_down2_num=int(''.join(map(str, station_down2)))
        #print('station_down2_num:',station_down2_num)
        walk_down2=abs(X-station_down2_num)
        result_down2=(len(station_down2)+walk_down2)

    variable_names = ['dsa', 'result', 'result_flag1', 'result_flag2', 'result_up','result_up2', 'result_down', 'result_down2','result_reverse','result_reverse2']

    # 로컬 변수들을 딕셔너리로 얻기
    local_variables = locals()

    # 존재하는 변수들만 필터링
    existing_variables = [var for var in variable_names if var in local_variables]
    #print(existing_variables)
    # 존재하는 변수들의 값 얻기
    existing_values = [local_variables[var] for var in existing_variables]
    #print(existing_values)
    # 존재하는 변수들 중 최솟값 찾기
    min_value = min(existing_values)
    print(min_value)

else: #버튼이 10개 모두 고장난상태
    print(dsa)














