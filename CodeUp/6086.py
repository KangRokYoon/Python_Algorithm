n = int(input())
s=0
x=0
while True:
    s += x
    x += 1
    if n <= s:
        break
print(s)