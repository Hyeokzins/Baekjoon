import sys
X = int(sys.stdin.readline())
if X == 1:
    print("1/1")
else:
    n = 1 
    while X > n: 
        X -= n 
        n += 1 
    if n % 2 == 0: 
        print("{}/{}".format(X, n-X+1))
    else: 
        print("{}/{}".format(n-X+1, X))