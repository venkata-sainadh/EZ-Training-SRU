l = list(map(int,input().split()))
k = int(input())
if k>len(l):
    k = k%len(l)
while k!=0:
    t = l[0]
    j=1
    while j<len(l):
        l[j-1] = l[j]
        j+=1
    l[j-1] = t
    k-=1
print(l)
    