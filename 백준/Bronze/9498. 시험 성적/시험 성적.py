import sys
N = int(sys.stdin.readline().rstrip())

if N<=100 and N>=90:
    print('A')

elif N<90 and N>=80:
    print('B')
elif N<80 and N>=70:
    print('C')
elif N<70 and N>=60:
    print('D')
else:
    print('F')
