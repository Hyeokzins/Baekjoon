import sys
N=int(sys.stdin.readline().rstrip())  #명령내릴 횟수를 입력받아 저장
word_list=[]
for i in range(N):
    word=(sys.stdin.readline().rstrip())
    if word not in word_list:
        word_list.append(word)

    else:
        continue

word_list.sort(key=lambda x: (len(x), x))



for i in range(len(word_list)):
    print(word_list[i])

