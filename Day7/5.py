def subsets(nums):
    outer = [[]]
    for i in nums:
        n = len(outer)
        for j in range(n):
            internal = outer[j].copy()
            if i not in internal:
                internal.append(i)
                internal.sort()
            if internal not in outer:
                outer.append(internal)
    return outer
nums = [1,2,3]
print(subsets(nums))


import itertools
res = itertools.combinations(nums,1) #1 is no.of elements to be considered
for i in res:
    print(list(i),end = ' ')
print()
res  = itertools.permutations(nums)
dc=0
for i in res:
    print(list(i),end = " ")
    dc+=1
print("\nNumber of permutations in res = ",dc)