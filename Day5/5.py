def subsetsprint(res,l,ans):
    if len(l)==0:
        ans.append(res)
        return ans
    ans = subsetsprint(res+l[0:1],l[1:],ans)
    ans = subsetsprint(res,l[1:],ans)
    return ans
l = [1,2,3]
ans = []
res = []
print(subsetsprint(res,l,ans))