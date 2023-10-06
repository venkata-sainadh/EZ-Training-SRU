n = int(input("Enter a number = "))
if n<0:
    n = -(n+1)
dc = 0
while(n):
    dc+=1
    n = n&(n-1)
print(dc)
