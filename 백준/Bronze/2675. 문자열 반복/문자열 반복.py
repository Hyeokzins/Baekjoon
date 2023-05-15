import sys
N= int(sys.stdin.readline())
re_word_list=[]

re_word=''
for i in range(N):
    num,word=sys.stdin.readline().split()

    for j in range(len(word)):
        re_word=re_word+word[j]*int(num)
    re_word_list.append(re_word)
    re_word=''


for i in range(len(re_word_list)):
    print(re_word_list[i])

    
    
