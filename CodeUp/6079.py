n= int(input())
s= 0
for i in range(0, 1001):
    s+=i
    if s >= n:
        break
print(i)