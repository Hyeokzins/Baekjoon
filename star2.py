a=int(input())

if a>=1 and a<=100:
    for i in range(a):
        print(" " * int(a-i-1) +'*'*int(i+1))
    