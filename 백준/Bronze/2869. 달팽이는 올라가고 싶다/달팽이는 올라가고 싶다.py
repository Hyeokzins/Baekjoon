import sys
A,B,V = map(int,sys.stdin.readline().split())



day=(V-A)/(A-B)

if day>int(day):
    print(int(day)+2)
else:
    print(int(day)+1)