a=input().upper()
alphabet_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count=[]
for i in (alphabet_list):
    count.append(a.count(i))


if count.count(max(count))>1:
    print("?")
else:
    print(alphabet_list[count.index(max(count))])

