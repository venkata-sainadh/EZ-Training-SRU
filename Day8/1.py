def quicksort(l,start,end):
    if start<end:
        i = start
        j = end
        pivot = start
        while i<j:
            while i<end and l[i]<=l[pivot]:
                i+=1
            while j>0 and l[j]>l[pivot]:
                j-=1
            if i<j:
                l[i],l[j] = l[j],l[i]
            l[pivot],l[j] = l[j],l[pivot]
            quicksort(l,start,pivot-1)
            quicksort(l,pivot+1,end)
print(quicksort([3,2,4,5,1],0,4))