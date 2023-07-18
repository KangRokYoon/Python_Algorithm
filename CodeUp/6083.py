a, b, c = map(int,input().split())

for i in range (0,a):
    for j in range(0,b):
        for k in range(0,c):
            print(i,j,k, end="\n")
print(a*b*c)