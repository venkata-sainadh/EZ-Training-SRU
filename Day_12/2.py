class parent:
    def fun1(self):
        print("Iam Your parent")
class child1(parent):
    def fun2(self):
        print("Iam the child")
ob = child1()s1 = input()
s2 = input()
res = []
for i in range(len(s1)):
    for j in range(i+1,len(s1)):
        ans = ""
        for k in range(i,j+1):
            ans+=s1[k]
        res.append(ans)
ans = ""
for i in res:
    if i in s2:
        # print(i)
        if len(i)>len(ans):
            ans = i
print(ans)
ob.fun1()