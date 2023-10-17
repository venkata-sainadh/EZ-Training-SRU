def sumtar(l,tar,i,j):
    if l[i]==tar:
        return [l[0]]
    j = 0
    cs = l[i]
    while j<len(l)-1:
        if cs==tar:
            return l[i:j+1]
        elif j<len(l) and cs<tar:
            j+=1
            cs+=l[j]
        elif cs>tar:
            cs-=l[i]
            i+=1
    return None

l = list(map(int,input().split()))
tar = int(input())
print(sumtar(l,tar,0,0))