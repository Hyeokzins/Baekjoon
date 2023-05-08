A=input()
B=input()
calculate=[int(A)*int(i) for i in B[::-1]]

calculate_sum=[calculate[i]*10**i for i in range(len(calculate))]
for i in range(len(calculate)):
    print(calculate[i])
print(sum(calculate_sum))
